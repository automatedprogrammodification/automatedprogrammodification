package gin.util;

import java.io.File;
import java.io.FileReader;
import org.apache.commons.io.FileUtils;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.nio.charset.Charset;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.AbstractMap.SimpleEntry;
import java.util.Map;
import java.util.Map.Entry;
import java.util.concurrent.TimeoutException;
import java.text.ParseException;

import com.opencsv.CSVReaderHeaderAware;
import com.sampullara.cli.Args;
import com.sampullara.cli.Argument;
import org.pmw.tinylog.Logger;
import org.zeroturnaround.exec.ProcessExecutor;
import org.apache.commons.lang3.tuple.Triple;
import org.apache.commons.lang3.tuple.ImmutableTriple;

import gin.Patch;
import gin.SourceFileLine;
import gin.SourceFileTree;
import gin.edit.Edit;
import gin.edit.Edit.EditType;
import gin.test.UnitTestResultSet;

/**
 * Runs all tests found in the methodFile for a given project through Gin. 
 *
 * Required input: projectDirectory, methodFile, projectName (Gradle/Maven)
 * Required input: projectDirectory, methodFile, classPath (otherwise)
 * 
 * methodFile will usually be the output file of gin.util.Profiler
 * outputFile will usually be the output file of a class extending gin.util.Sampler
 *
 * patchFile: this will be the edits_overlaps_all.csv file found in the data folder after outputs of RandomSampler have been processed using runScripts.sh
 */
public class PatchTester extends Sampler{

    @Argument(alias = "patchFile", description = "File with a list of patches (usually output of gin.util.Sampler)")
    protected File patchFile;

    protected List<Triple<String, Integer, String>> patchData = new ArrayList<>();

    protected long analyseNumber = 0;
    protected long cpfp = 0;

    public static void main(String[] args) {
        PatchTester sampler = new PatchTester(args);
        sampler.sampleMethods();
    }

    public PatchTester(String[] args) {
        super(args);
        Args.parseOrExit(this, args);
        printAdditionalArguments();
        this.patchData = processPatchFile();
        if (patchData.isEmpty()) {
            Logger.info("No patches to process.");
            System.exit(0);
        }
    }

    // Constructor used for testing
    public PatchTester(File projectDir, File methodFile, File patchFile) {
        super(projectDir, methodFile);
        this.patchFile = patchFile;
    }

    private void printAdditionalArguments() {
        Logger.info("Patch file: "+ patchFile);
    }

    protected void sampleMethods() {
        
        writeHeader();

        for (Triple<String, Integer, String> entry : patchData) {

            String patchText = entry.getLeft();
            Integer methodID = entry.getMiddle();
	    String editCompiled = entry.getRight();

            TargetMethod method = null;

            for (TargetMethod m : methodData) {
                if (m.getMethodID().equals(methodID)) {
                    method = m;
                    break;
                }
            }
           
            if (method == null) {

                Logger.info("Method with ID: " + methodID.toString() + " not found for patch " + patchText);

            } else { 

                // Get method location
                File source = method.getFileSource();
                String className = method.getClassName();

                // Create source files for edits for the  method
                SourceFileLine sourceFileLine = new SourceFileLine(source.getPath(), null);
                SourceFileTree sourceFileTree = new SourceFileTree(source.getPath(), null);
                
                // Parse patch
                Patch patch = parsePatch(patchText, sourceFileLine, sourceFileTree, editCompiled);

		Logger.info("Analyse number: " + analyseNumber);
		Logger.info("CPFP number: " + cpfp);

            }

        }

        Logger.info("Results saved to: " + super.outputFile.getAbsolutePath());
    }

    private List<Triple<String,Integer,String>> processPatchFile() {

        try {
            CSVReaderHeaderAware reader = new CSVReaderHeaderAware(new FileReader(patchFile));
            Map<String, String> data = reader.readMap();
            if ( (!data.containsKey("Patch")) || (!data.containsKey("MethodIndex")) || (!data.containsKey("Project")) || (!data.containsKey("EditCompiled")) ) {
                throw new ParseException("\"Patch\", \"MethodIndex\", \"EditCompiled\", and \"Project\" fields are required in the patch file.", 0);
            }

            List<Triple<String,Integer,String>> patches = new ArrayList<>();

            while (data != null) {

		if ((data.get("Project")).equals(this.projectName)) {
                    String patch = data.get("Patch");
                    Integer methodID = Integer.valueOf(data.get("MethodIndex"));
		    String editCompiled = data.get("EditCompiled");
                    patches.add(new ImmutableTriple(patch, methodID, editCompiled));
		}

                data = reader.readMap();
            }        
            reader.close();

            return patches;

        } catch (ParseException e) {
            Logger.error(e.getMessage());
            Logger.trace(e);
        } catch (IOException e) {
            Logger.error("Error reading patch file: " + patchFile);
            Logger.trace(e);
        }
        return new ArrayList<>();

    }

    private Patch parsePatch(String patchText, SourceFileLine sourceFileLine, SourceFileTree sourceFileTree, String editCompiled) {

        List<Edit> editInstances = new ArrayList<>();
        
        String patchTrim = patchText.trim();
        String cleanPatch = patchTrim;

        if (patchTrim.startsWith("|")) {
            cleanPatch = patchText.replaceFirst("\\|", "").trim();
        }

        String[] editStrings = cleanPatch.trim().split("\\|");
        
        boolean allLineEdits = true;
        boolean allStatementEdits = true;
        
        for (String editString: editStrings) {

            String[] tokens = editString.trim().split("\\s+");

            String editAction = tokens[0];

            Class<?> clazz = null;

            try {
                clazz = Class.forName(editAction);
            } catch (ClassNotFoundException e) {
                Logger.error("Patch edit type unrecognised: " + editAction);
                Logger.trace(e);
                System.exit(-1);
            }

            Method parserMethod = null;
            try {
                parserMethod = clazz.getMethod("fromString", String.class);
            } catch (NoSuchMethodException e) {
                Logger.error("Patch edit type has no fromString method: " + clazz.getCanonicalName());
                Logger.trace(e);
                System.exit(-1);
            }

            Edit editInstance = null;
            try {
                editInstance = (Edit) parserMethod.invoke(null, editString.trim());
            } catch (IllegalAccessException e) {
                Logger.error("Cannot parse patch: access error invoking edit class.");
                Logger.trace(e);
                System.exit(-1);
            } catch (InvocationTargetException e) {
                Logger.error("Cannot parse patch: invocation error invoking edit class.");
                Logger.trace(e);
                System.exit(-1);
            }

            allLineEdits &= editInstance.getEditType() == EditType.LINE;
            allStatementEdits &= editInstance.getEditType() != EditType.LINE;
            editInstances.add(editInstance);
            
        }
        
        if (!allLineEdits && !allStatementEdits) {
            Logger.error("Cannot proceed: mixed line/statement edit types found in patch");
            System.exit(-1);
        }
        
        Patch patch = new Patch(allLineEdits ? sourceFileLine : sourceFileTree);

        String original = patch.getSourceFile().toString();
        try {
            FileUtils.writeStringToFile(new File("source.original"), original, Charset.defaultCharset());
        } catch (IOException e) {
            Logger.error("Could not write original source.");
            Logger.trace(e);
            System.exit(-1);
        }

	List<String> patchedSources = new ArrayList<>();
	patchedSources.add(original);
	boolean seen = false;
	char pre = 'P';
	char nex = 'P';
	String patched = patch.apply();
	assert(editInstances.size() == editCompiled.length());
        for (int i=0; i < editInstances.size(); i++) {
	    Edit e = editInstances.get(i);
	    nex = editCompiled.charAt(i);
            patch.add(e);
            patched = patch.apply();
            //Logger.info("Added next edit: " + e.toString());
	    //if (nex=='P' && (pre=='C' || pre=='F')) {
	    // only F considered
	    if (nex=='P' && pre=='F') {
		cpfp += 1;
	        for (String previous : patchedSources) {
		    if (isPatchedSourceSame(previous, patched)) {
		        seen = true;
		    } 
	        }

		if (!seen) {

	    		analyseNumber++;

            		try {
            		    FileUtils.writeStringToFile(new File("source.patched1"), patchedSources.get(patchedSources.size()-1), Charset.defaultCharset());
            		} catch (IOException ex) {
            		    Logger.error("Could not write patched source.");
            		    Logger.trace(ex);
            		    System.exit(-1);
            		}

            		try {
            		    FileUtils.writeStringToFile(new File("source.patched2"), patched, Charset.defaultCharset());
            		} catch (IOException ex) {
            		    Logger.error("Could not write patched source.");
            		    Logger.trace(ex);
            		    System.exit(-1);
            		}
			Logger.info("First diff:");
            		try {
            		    String output = new ProcessExecutor().command("diff", "source.original", "source.patched1")
            		              .readOutput(true).execute()
            		              .outputUTF8(); 
            		    Logger.info(output);
            		} catch (IOException ex) {
            		    Logger.trace(ex);
            		    System.exit(-1);
            		} catch (InterruptedException ex) {
            		    Logger.trace(ex);
            		    System.exit(-1);
            		} catch (TimeoutException ex) {
            		    Logger.trace(ex);
            		    System.exit(-1);
            		}
			Logger.info("Second diff:");
            		try {
            		    String output = new ProcessExecutor().command("diff", "source.original", "source.patched2")
            		              .readOutput(true).execute()
            		              .outputUTF8(); 
            		    Logger.info(output);
            		} catch (IOException ex) {
            		    Logger.trace(ex);
            		    System.exit(-1);
            		} catch (InterruptedException ex) {
            		    Logger.trace(ex);
            		    System.exit(-1);
            		} catch (TimeoutException ex) {
            		    Logger.trace(ex);
            		    System.exit(-1);
            		}

		    }
	    }
	    seen = false;
	    patchedSources.add(patched);
	    pre = nex;

        }

        return patch;

    }

    protected boolean isPatchedSourceSame(String original, String patchedSource) {
        String normalisedPatched = patchedSource.replaceAll("//.*\\n", "");
        String normalisedOriginal = original.replaceAll("//.*\\n", "");
        normalisedPatched = normalisedPatched.replaceAll("\\s+", " ");
        normalisedOriginal = normalisedOriginal.toString().replaceAll("\\s+", " ");
        normalisedOriginal = normalisedOriginal.toString().replaceAll("\\s+", " ");
        boolean noOp = normalisedPatched.equals(normalisedOriginal);
        return noOp;
    }
}
