import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.lang.ProcessBuilder.Redirect;
import java.nio.file.Files;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import gin.SourceFileLine;

public class AddCyclomaticComplexity {

	static final Pattern FILENAME_IN_EDIT = Pattern.compile(" \\S+.java");
	
	public static void main(String[] args) throws IOException {

		String methodList = "AllMethods2.txt";
		String output = "StatsFromCheckstyle2.csv";
		
		String[] githubProjects = new String[]{
                "arthas",
                "disruptor",
                "druid",
                "gson",
                "jcodec",
                "junit",
                "ibatis",
                "opennlp",
                "spark",
                "spatial4j"
            };
		
		String[] projectPaths = new String[] {
				"/home/oldchap/gin/casestudies/arthas/core/src/main/java/",
				"/home/oldchap/gin/casestudies/disruptor/src/main/java/",
				"/home/oldchap/gin/casestudies/druid/src/main/java/",
				"/home/oldchap/gin/casestudies/gson/gson/src/main/java/",
				"/home/oldchap/gin/casestudies/jcodec/src/main/java/",
				"/home/oldchap/gin/casestudies/junit4/src/main/java/",
				"/home/oldchap/gin/casestudies/mybatis-3/src/main/java/",
				"/home/oldchap/gin/casestudies/opennlp/opennlp-tools/src/main/java/",
				"/home/oldchap/gin/casestudies/spark/src/main/java/",
				"/home/oldchap/gin/casestudies/spatial4j/src/main/java/"
		};
		
		getMethodLine("com.lmax.disruptor.Sequence.compareAndSet(long,long)", githubProjects, projectPaths);
		

		List<String> methods = Files.readAllLines(new File(methodList).toPath());
		
		PrintStream out = new PrintStream(new FileOutputStream(output));
		out.println("method,cyclomatic,ncss,npath");
		int i = 0;
		for (String method : methods) {
			System.out.println("Processing " + ++i + "/" + methods.size() + ": " + method);
			Object[] lineNumber = getMethodLine(method, githubProjects, projectPaths);
			int[] metrics = checkCyclomatic((String)lineNumber[0], (Integer)lineNumber[1]);
			out.println("\"" + method + "\"," + metrics[0] + "," + metrics[1] + "," + metrics[2]);
		}
		
		out.close();
		
	
	}

	private static Pattern ccPattern = Pattern.compile(".*Cyclomatic Complexity is (\\d+)");
	private static Pattern ncssPattern = Pattern.compile(".*NCSS for this method is (\\d+)");
	private static Pattern npathPattern = Pattern.compile(".*NPath Complexity is (\\d+)");
	
	public static int[] checkCyclomatic(String javaSourceFile, int lineNumber) {
		ProcessBuilder pb = new ProcessBuilder("java", "-jar", "checkstyle-8.36.2-all.jar", "-c", "checks.xml", "-d", javaSourceFile);

		int cc = -1;
		int ncss = -1;
		int npath = -1;
		
		try {
	        final Process process = pb.redirectError(Redirect.INHERIT).redirectInput(Redirect.INHERIT).start();
	        final Scanner scanner = new Scanner(process.getInputStream());
	        while (scanner.hasNextLine()) {
	            String line = scanner.nextLine();
	            if (line.contains("[CyclomaticComplexity]") && line.contains(".java:"+lineNumber+":")) {
	            	//System.out.println(line);

	            	Matcher m = ccPattern.matcher(line);
	            	if (m.find()) {
	            		cc = Integer.parseInt(m.group(1));
	            		//System.out.println("CC:" + cc);
	            	}
	            }
	            
	            if (line.contains("[JavaNCSS]") && line.contains(".java:"+lineNumber+":")) {
	            	//System.out.println(line);

	            	Matcher m = ncssPattern.matcher(line);
	            	if (m.find()) {
	            		ncss = Integer.parseInt(m.group(1));
	            		//System.out.println("NCSS:" + ncss);
	            	}
	            }
	            
	            if (line.contains("[NPathComplexity]") && line.contains(".java:"+lineNumber+":")) {
	            	//System.out.println(line);

	            	Matcher m = npathPattern.matcher(line);
	            	if (m.find()) {
	            		npath = Integer.parseInt(m.group(1));
	            		//System.out.println("NCSS:" + ncss);
	            	}
	            }
	            
	            if ((cc > -1) && (ncss > -1) && (npath > -1)) {
	            	return new int[] {cc, ncss, npath};
	            }
	        }
		} catch (Exception e) {
			e.printStackTrace();
		}
		
        return new int[] {cc, ncss, npath};
	}
	
	public static Object[] getMethodLine(String methodFqName, String[] githubProjects, String[] projectPaths) {
		int projectIndex = -1;
		for (int i = 0; i < projectPaths.length; i++) {
			if (methodFqName.contains(githubProjects[i])) {
				projectIndex = i;
				break;
			}
		}
		
		
		String methodFqNameMinusArgs = methodFqName.substring(0, methodFqName.lastIndexOf("("));
		String className = projectPaths[projectIndex] + methodFqNameMinusArgs.substring(0, methodFqNameMinusArgs.lastIndexOf(".")).replace(".", "/") + ".java";
		//String methodName = methodFqName.substring(methodFqNameMinusArgs.lastIndexOf(".") + 1);
		//System.out.println(className + "   " + methodName);
		SourceFileLine sfl = new SourceFileLine(className, Collections.singletonList(methodFqName));
		List<Integer> ids = sfl.getLineIDsInTargetMethod();
		//System.out.println(ids);
		
		return new Object[] {className, ids.get(0)};
	}
}
