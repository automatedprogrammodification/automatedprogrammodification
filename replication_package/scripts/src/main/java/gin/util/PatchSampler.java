package gin.util;

import java.io.File;
import java.lang.Math;
import java.util.List;
import java.util.ArrayList;
import java.util.Random;
import java.util.Map.Entry;
import java.util.AbstractMap;

import com.sampullara.cli.Args;
import com.sampullara.cli.Argument;
import org.pmw.tinylog.Logger;

import gin.Patch;
import gin.SourceFile;
import gin.SourceFileLine;
import gin.SourceFileTree;
import gin.edit.Edit;
import gin.edit.Edit.EditType;
import gin.edit.line.DeleteLine;
import gin.edit.line.CopyLine;
import gin.edit.line.ReplaceLine;
import gin.edit.line.SwapLine;
import gin.edit.statement.DeleteStatement;
import gin.edit.statement.CopyStatement;
import gin.edit.statement.ReplaceStatement;
import gin.edit.statement.SwapStatement;

/**
 * Calculates all edits of a given type
 */
public class PatchSampler extends Sampler {

    @Argument(alias = "et", description = "Edit type")
    protected EditType editType = EditType.LINE;

    private long editTotal = 0;
    private long deleteTotal = 0;

    public static void main(String[] args) {

        PatchSampler sampler = new PatchSampler(args);
        sampler.sample();
    }

    public PatchSampler(String[] args) {

        super(args);
        Args.parseOrExit(this, args);
        printAdditionalArguments();
    }

    public PatchSampler(File projectDir, File methodFile) {

        super(projectDir, methodFile);
        printAdditionalArguments();
    }

    private void printAdditionalArguments() {

        Logger.info("Edit type: "+ editType);
    }

    protected void sample() {

        if ((editType == EditType.LINE) || (editType == EditType.STATEMENT)){
            Logger.info("Sampling methods..");
            sampleMethods();
        } else {
            Logger.info("Currently only the following edit types are supported: LINE and STATEMENT.");
        }
    }


    @Override
    protected void sampleMethods() {

        for (TargetMethod targetMethod : methodData) {

            File source = targetMethod.getFileSource();
            String methodName = targetMethod.getMethodName();

            SourceFile sourceFile;
            List<Integer> sourceLocations;
            List<Integer> targetLocations;
            List<Entry<Integer, Integer>> targetInsertLocations = new ArrayList<>();
            int tCopyl; // target insert locations for the Copy operator
            int sReplaceSwapl = 0; // source locations for Replace and Swap for method statement operators

            if (editType == EditType.LINE) {

                SourceFileLine sourceFileLine = new SourceFileLine(source, methodName);
                sourceLocations = sourceFileLine.getLineIDsNonEmptyOrComments(false);
                targetLocations = sourceFileLine.getLineIDsNonEmptyOrComments(true);
                tCopyl = targetLocations.size();
                sourceFile = sourceFileLine;

            } else { // STATEMENT

                SourceFileTree sourceFileTree = new SourceFileTree(source, methodName);
                sourceLocations = sourceFileTree.getAllStatementIDs(); 
                targetLocations = sourceFileTree.getStatementIDsInTargetMethod(); 
                for (Integer blockID : sourceFileTree.getBlockIDsInTargetMethod()) {
                    for (Integer stmtID : sourceFileTree.getInsertionPointsInBlock(blockID)) {
                        targetInsertLocations.add(new AbstractMap.SimpleImmutableEntry(blockID, stmtID));
                    }
                }
                tCopyl = targetInsertLocations.size();
                sourceFile = sourceFileTree;

            }
 
            int sl = sourceLocations.size(); 
            int tl = targetLocations.size();

            String filename = sourceFile.getFilename();

            int startCopy = tl; // number of delete edits
            int startReplace = Math.addExact(startCopy, Math.multiplyExact(sl, tCopyl)); // number of copy edits
            int startSwap;
            int noOfEdits;
            startSwap = Math.addExact(startReplace, Math.multiplyExact(sl, tl));  // number of replace edits
            noOfEdits = Math.addExact(startSwap, Math.multiplyExact(tl, tl)); // number of swap edits

            editTotal = Math.addExact(noOfEdits, editTotal);
            deleteTotal = Math.addExact(tl, deleteTotal);

        }

        Logger.info("Total number of " + editType + " edits for project: " + editTotal);                
        Logger.info("Total number of " + editType + " deletions for project: " + deleteTotal);          

    }

}
