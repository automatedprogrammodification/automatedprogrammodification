
import soot.*;
import soot.jimple.InvokeStmt;
import soot.jimple.JimpleBody;
import soot.options.Options;
import soot.toolkits.graph.TrapUnitGraph;
import soot.toolkits.graph.UnitGraph;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.IOException;

public class DefUse {
    public static String sourceDirectory = System.getProperty("user.dir");
    public static String clsName = "NullPointerExample";
    public static String methodName;
    public static String classPath;

    public static void setupSoot(String className) {
        G.reset();// set class path here.
	String jreDir = System.getProperty("java.home") + "/lib/jce.jar";
	String jceDir = System.getProperty("java.home") + "/lib/rt.jar";
	//System.out.println(jreDir);
	//System.out.println(classPath);
	String path = jreDir + File.pathSeparator+ jceDir + File.pathSeparator +
	    System.getProperty("user.dir") + File.pathSeparator + classPath;
	System.out.println(path);
	    //+ File.pathSeparator + "../../packages/arthas-master/core/target/classes/" +  File.pathSeparator + "../../packages/arthas-master/core/target/tmp_out/";
        Options.v().set_soot_classpath(path);
        Options.v().set_prepend_classpath(true); 
        Options.v().set_keep_line_number(true);
        Options.v().set_keep_offset(true);
        //Options.v().set_soot_classpath("../../packages/arthas-master/core/target/classes/"); // doesn't work

	// go to class name.
	clsName=className; // argument 0 to the program.
	System.out.println("here");
        SootClass sc = Scene.v().loadClassAndSupport(clsName);
        sc.setApplicationClass();
        Scene.v().loadNecessaryClasses(); // finished setup. 
    }

    private static String normSigTypeString(String sig){
	// extracts a comma separated list of types from sig
	// strips away all but the core type
	// e.g. List from java.util.List<Integer>

	//System.out.println("vals");
	//System.out.println(sig.split("\\(")[1]);
	String[] tmps=sig.split("\\("); // get parm list
	String res=tmps[1];
	tmps=res.split("\\)"); // strip off last bracket
	if(tmps.length<1){
	    return "";
	}
	res=tmps[0];
	tmps=res.split("\\,"); // get each parameter
	
	res=""; // build up this the string again
	for(String s:tmps){
	    String[] quals=s.split("\\.");
	    String tmp=quals[quals.length-1];
	    quals=tmp.split("<"); // get rid of generics
	    tmp=quals[0];
	    if(tmp.equals("T")){
		tmp="Object";  // kludge idiom for type vars
	    }
	    res+=tmp + ",";
	}
	res= res.substring(0, res.length() - 1); // remove last comma
	//System.out.println(res);
	return res;
    }


    public static void main(String[] args) throws IOException{
	Map <String,ArrayList<Integer>> defMap = new TreeMap <String,ArrayList<Integer>>(); // map of current defs Integer is a line number
	ArrayList<DefUseRecord<Integer,Integer>> defUseList =
	    new ArrayList<DefUseRecord<Integer,Integer>>(); // list of def use pairs
	
	classPath=args[2];
	setupSoot(args[0]);
	methodName=args[1];
	String methodIndex=args[3]; // used to build a better file name.
        String fullMethodName=args[4];
        SootClass mainClass = Scene.v().getSootClass(clsName); // get object
        for (SootMethod sm : mainClass.getMethods()) {
	    if(!(methodName.equals(sm.getName()))){
		continue;
	    }
            System.out.println("Method: " + sm.getSignature());
	    System.out.println("Name: " + sm.getName());
	    //System.out.println("Norm sig soot sig " +
	    //	       normSigTypeString(fullMethodName));
	    //System.out.println("Norm sig soot sig " +
	    //		       normSigTypeString(sm.getSignature()));

	    String normFullMethodName=normSigTypeString(fullMethodName);
	    String normSootSignature=normSigTypeString(sm.getSignature());
	    System.out.println(normFullMethodName);
	    System.out.println(normSootSignature);

	    if(normFullMethodName.equals(normSootSignature)){
		System.out.println("SAME!!!");
	    }else{
		System.out.println("NOT SAME!!!");
		continue;
	    }

	    
            JimpleBody body = (JimpleBody) sm.retrieveActiveBody(); // grab body
            UnitGraph unitGraph = new TrapUnitGraph(body); // grad method body
            int statCount=0;
            for(Unit unit : body.getUnits()){
                statCount++;
		// defs
		
		for(ValueBox defValueBox: unit.getDefBoxes()){
		    if(defValueBox.getValue() instanceof Local){
		        Local usedLocal = (Local) defValueBox.getValue();
		    //Value usedLocal =  usedValueBox.getValue();
			//System.out.println("    Line " + unit.getJavaSourceStartLineNumber() +": " +  "uses of local " + usedLocal + " in unit " + unit);
			int lineNum=unit.getJavaSourceStartLineNumber();
			System.out.print("    Line " +
				   unit.getJavaSourceStartLineNumber());
			System.out.println(" defines local " + usedLocal);
			// add to the def-map list
			if(defMap.get(usedLocal.getName())==null){
			    ArrayList<Integer> vals=new ArrayList<Integer>();
			    vals.add(lineNum);
			    defMap.put(usedLocal.getName(),vals);
			}else{
			    ArrayList<Integer> vals=
				defMap.get(usedLocal.getName());
			    vals.add(lineNum);
			}
		     }
		}


		
		// change map into list of def-use entries. 
                for(ValueBox usedValueBox : unit.getUseBoxes()){
                    if(usedValueBox.getValue() instanceof Local){
		        Local usedLocal = (Local) usedValueBox.getValue();
		    //Value usedLocal =  usedValueBox.getValue();
			//System.out.println("    Line " + unit.getJavaSourceStartLineNumber() +": " +  "uses of local " + usedLocal + " in unit " + unit);
			int lineNumUse = unit.getJavaSourceStartLineNumber();
			System.out.print("    Line " +
				   lineNumUse);
			System.out.println(" uses local " + usedLocal);
			
			// look up def and make pair to add to list
			// of def-use pair line numbers.
			ArrayList<Integer> vals =defMap.get(usedLocal.getName());
                        // iterate backwards from end
			int index=vals.size()-1;
			while((index>0) && (vals.get(index)>lineNumUse)){
			    // in case of multiple defs
			    index--;
			}
			Integer lineNumDef=vals.get(index);
			
		        //Integer lineNumDef = defMap.get(usedLocal.getName());
			DefUseRecord<Integer,Integer> entry =
			    new DefUseRecord<Integer,Integer>();
			// add entry to the defUseList. 
			entry.def=lineNumDef;
			entry.use=lineNumUse;
			entry.methodName=methodName;
			entry.className=clsName;
			defUseList.add(entry);
		 
		     }
                }
            }
        }

	// normalise defUseList entries
	
	// find minIndex
	int minLine=Integer.MAX_VALUE;
	for(DefUseRecord<Integer,Integer> entry:defUseList){
	    // check the use and def - only should need to check def
	    // but be conservative.
	    if(entry.use<minLine && entry.use!=-1){
		minLine=entry.use;
	    }
	    if(entry.def<minLine && entry.def!=-1){
		minLine=entry.def;
	    }
	}
	//System.out.println(minLine);
	
	// now normalise
	
	ArrayList<DefUseRecord<Integer,Integer>> resList =
	    new ArrayList<DefUseRecord<Integer,Integer>>();
	
        for(DefUseRecord<Integer,Integer> entry:defUseList){
	    if(entry.def==-1){
		entry.def=0;
	    }else{
		entry.def=entry.def-(minLine-1);
	    }
	    // now uses
	    if(entry.use==-1){
		entry.use=0;
	    }else{
		entry.use=entry.use-(minLine-1);
	    }
	    // now copy if not equal
	    if(entry.def!=entry.use){
		resList.add(entry);
	    }
	}

       
	// write the defUseList out to a file
	String fileName = "defUseRecordsNew/" + clsName + "." + methodName + "_" + 
	     methodIndex +".csv";
	// set up a print writer
	FileWriter myFile= new FileWriter(fileName);
	PrintWriter pFile= new PrintWriter(myFile);

	pFile.print("className,methodName,defLine,useLine");
	pFile.println();
	// print out records
	for(int i=0; i<resList.size();i++){
	    // get the record
	    DefUseRecord<Integer,Integer> entry =
		resList.get(i);
	    // make the record
	    String line = entry.className + "," +
		entry.methodName + "," +
		entry.def + "," +
		entry.use;
	    // print the line
	    pFile.print(line);
	    pFile.println();
	}
	// now add code to nomalise to map the first line to line 1 and -1
	// to line zero.
	// also double check that -1 is refering to variables outside of
	// of the local variables (easy to do by looking at the line numbers)
	pFile.close();
    }
}

class DefUseRecord<A, B> {
    public  String className;
    public  String methodName;
    public  A def;
    public  B use;
}
