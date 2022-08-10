Feature Analysis
==========

The following are direct links to the specific versions of each of the projects in the study
- [Arthas](https://github.com/alibaba/arthas/tree/arthas-all-3.0.5)
- [Disruptor](https://github.com/LMAX-Exchange/disruptor/tree/3.4.2)
- [Druid](https://github.com/alibaba/druid/tree/1.1.11)
- [Gson](https://github.com/google/gson/tree/gson-parent-2.8.5)
- [JCodec](https://github.com/jcodec/jcodec/tree/v0.2.3)
- [JUnit4](https://github.com/junit-team/junit4/tree/r4.13-beta-2)
- [Mybatis-3](https://github.com/mybatis/mybatis-3/tree/mybatis-3.4.6)
- [OpenNLP](https://github.com/apache/opennlp/tree/opennlp-1.7.0)
- [Spatial4J](https://github.com/locationtech/spatial4j/tree/spatial4j-0.7)
- [Spark](https://github.com/perwendel/spark/tree/2.7.2)


The following are direct links to the versions of the methods that we categorised as "upstanding citizens" or "rogues' gallery"

Upstanding Citizens: Predictably APM-able (Statement Operators)
-------
| Project   | MethodName                                                                                                                                         | Pass Rate |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| druid     | [com.alibaba.druid.sql.dialect.hive.parser.HiveStatementParser.createSQLSelectParser()](https://github.com/alibaba/druid/blob/1.1.11/src/main/java/com/alibaba/druid/sql/dialect/hive/parser/HiveStatementParser.java#L46)                                                              | 44%       |
| gson      | [com.google.gson.stream.JsonWriter.name(String)](https://github.com/google/gson/blob/gson-parent-2.8.5/gson/src/main/java/com/google/gson/stream/JsonWriter.java#L168)                                                                                                     | 46%       |
| jcodec    | [org.jcodec.codecs.h264.decode.Intra16x16PredictionBuilder.predictWithMode(int,int\[\]\[\],boolean,boolean,byte\[\],byte\[\],byte\[\],int,byte\[\])](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/h264/decode/Intra16x16PredictionBuilder.java#L18) | 50%       |
| druid     | com.alibaba.druid.sql.dialect.sqlserver.visitor.SQLServerOutputVisitor.visit(SQLExprTableSource)                                                   | 47%       |
| jcodec    | org.jcodec.codecs.h264.decode.BlockInterpolator.getBlockLuma(Picture,Picture,int,int,int,int,int)                                                  | 44%       |
| druid     | com.alibaba.druid.pool.DruidPooledConnection.checkState()                                                                                          | 40%       |
| jcodec    | org.jcodec.codecs.h264.decode.ChromaPredictionBuilder.predictWithMode(int\[\]\[\],int,int,boolean,boolean,byte\[\],byte\[\],byte\[\],byte\[\])     | 50%       |
| spatial4j | org.locationtech.spatial4j.context.jts.JtsSpatialContextFactory.checkDefaultFormats()                                                              | 44%       |
| druid     | com.alibaba.druid.sql.dialect.oracle.parser.OracleExprParser.partitionClauseRest(SQLPartitionBy)                                                   | 58%       |
| opennlp   | opennlp.tools.namefind.DefaultNameContextGenerator.getContext(int,String\[\],String\[\],Object\[\])                                                | 47%       |
| druid     | com.alibaba.druid.sql.dialect.mysql.visitor.MySqlOutputVisitor.visit(SQLExprTableSource)                                                           | 50%       |
| druid     | com.alibaba.druid.sql.dialect.mysql.parser.MySqlSelectParser.parseTableSourceRest(SQLTableSource)                                                  | 57%       |
| jcodec    | org.jcodec.codecs.h264.encode.DumbRateControl.accept(int)                                                                                          | 53%       |
| gson      | com.google.gson.stream.JsonWriter.beforeValue()                                                                                                    | 61%       |
| mybatis-3 | org.apache.ibatis.builder.MapperBuilderAssistant.setCurrentNamespace(String)                                                                       | 53%       |
| junit4    | org.junit.internal.AssumptionViolatedException.describeTo(Description)                                                                             | 63%       |
| spatial4j | org.locationtech.spatial4j.context.SpatialContextFactory.checkDefaultFormats()                                                                     | 55%       |

Old Data:
--------
- druid: [com.alibaba.druid.sql.dialect.oracle.parser.OracleExprParser.partitionClauseRest(SQLPartitionBy&#41;](https://github.com/alibaba/druid/blob/1.1.11/src/main/java/com/alibaba/druid/sql/dialect/oracle/parser/OracleExprParser.java#L1845)

- druid: [com.alibaba.druid.sql.dialect.mysql.visitor.MySqlOutputVisitor.visit(SQLExprTableSource&#41;](https://github.com/alibaba/druid/blob/1.1.11/src/main/java/com/alibaba/druid/sql/dialect/mysql/visitor/MySqlOutputVisitor.java#L2574)

- druid: [com.alibaba.druid.sql.dialect.mysql.parser.MySqlSelectParser.parseTableSourceRest(SQLTableSource&#41;](https://github.com/alibaba/druid/blob/1.1.11/src/main/java/com/alibaba/druid/sql/dialect/mysql/parser/MySqlSelectParser.java#L449)

- gson: [com.google.gson.stream.JsonWriter.beforeValue(&#41;](https://github.com/google/gson/blob/gson-parent-2.8.5/gson/src/main/java/com/google/gson/stream/JsonWriter.java#L628)

- mybatis-3: [org.apache.ibatis.builder.xml.XMLConfigBuilder.settingsElement(Properties&#41;](https://github.com/mybatis/mybatis-3/blob/mybatis-3.4.6/src/main/java/org/apache/ibatis/builder/xml/XMLConfigBuilder.java#L238)

- spatial4j: [org.locationtech.spatial4j.context.SpatialContextFactory.checkDefaultFormats(&#41;](https://github.com/locationtech/spatial4j/blob/spatial4j-0.7/src/main/java/org/locationtech/spatial4j/context/SpatialContextFactory.java#L247)

- mybatis-3: [org.apache.ibatis.builder.xml.XMLMapperBuilder.bindMapperForNamespace(&#41;](https://github.com/mybatis/mybatis-3/blob/mybatis-3.4.6/src/main/java/org/apache/ibatis/builder/xml/XMLMapperBuilder.java#L398)



Upstanding Citizens: non-APM-able
-------
- jcodec: [org.jcodec.codecs.h264.io.CABAC.readIntraChromaPredMode(MDecoder,int,MBType,MBType,boolean,boolean&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/h264/io/CABAC.java#L417)

- opennlp: [opennlp.tools.ml.model.ComparableEvent.compareTo(ComparableEvent&#41;](https://github.com/apache/opennlp/blob/opennlp-1.7.0/opennlp-tools/src/main/java/opennlp/tools/ml/model/ComparableEvent.java#L45)

- jcodec: [org.jcodec.codecs.h264.decode.SliceReader.readPredictionI4x4Block(boolean,boolean,MBType,MBType,int,int,int&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/h264/decode/SliceReader.java#L249)

- spark: [spark.utils.MimeParse.fitnessAndQualityParsed(String,Collection$<$ParseResults$>$&#41;](https://github.com/perwendel/spark/blob/2.7.2/src/main/java/spark/utils/MimeParse.java#L138)

- arthas: [com.taobao.arthas.core.util.TokenUtils.findSecondTokenText(List$<$CliToken$>$&#41;](https://github.com/alibaba/arthas/blob/arthas-all-3.0.5/core/src/main/java/com/taobao/arthas/core/util/TokenUtils.java#L56)



Rogues Gallery: APM-able
-------
- junit4: [org.junit.internal.runners.ClassRoadie.runAfters(&#41;](https://github.com/junit-team/junit4/blob/r4.13-beta-2/src/main/java/org/junit/internal/runners/ClassRoadie.java#L69)

- druid: [ com.alibaba.druid.pool.DruidPooledConnection.transactionRecord(String&#41;](https://github.com/alibaba/druid/blob/1.1.11/src/main/java/com/alibaba/druid/pool/DruidPooledConnection.java#L719)

- jcodec: [org.jcodec.codecs.h264.decode.BlockInterpolator.getLuma23(byte[],int,byte[],int,int,int,int,int,int&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/h264/decode/BlockInterpolator.java#L540)

- mybatis-3: [org.apache.ibatis.mapping.CacheBuilder.setStandardDecorators(Cache&#41;](https://github.com/mybatis/mybatis-3/blob/mybatis-3.4.6/src/main/java/org/apache/ibatis/mapping/CacheBuilder.java#L118)

- arthas: [com.taobao.arthas.core.view.ObjectView.renderObject(Object,int,int,StringBuilder&#41;](https://github.com/alibaba/arthas/blob/arthas-all-3.0.5/core/src/main/java/com/taobao/arthas/core/view/ObjectView.java#L97)


Rogues Gallery: non-APM-able
-------
- junit4: [junit.runner.BaseTestRunner.filterLine(String&#41;](https://github.com/junit-team/junit4/blob/r4.13-beta-2/src/main/java/junit/runner/BaseTestRunner.java#L303)

- gson: [com.google.gson.Gson.atomicLongArrayAdapter(TypeAdapter$<$Number$>$&#41;](https://github.com/google/gson/blob/gson-parent-2.8.5/gson/src/main/java/com/google/gson/Gson.java#L399)

- spark: [spark.staticfiles.StaticFilesConfiguration.configure(String&#41;](https://github.com/perwendel/spark/blob/2.7.2/src/main/java/spark/staticfiles/StaticFilesConfiguration.java#L140)

- opennlp: [opennlp.tools.util.AbstractEventStream.read(&#41;](https://github.com/apache/opennlp/blob/opennlp-1.7.0/opennlp-tools/src/main/java/opennlp/tools/util/AbstractEventStream.java#L54)

- opennlp: [opennlp.tools.postag.POSSampleEventStream.generateEvents(String[],String[],Object[],POSContextGenerator&#41;](https://github.com/apache/opennlp/blob/opennlp-1.7.0/opennlp-tools/src/main/java/opennlp/tools/postag/POSSampleEventStream.java#L73)

- mybatis-3: [org.apache.ibatis.builder.xml.XMLStatementBuilder.parseSelectKeyNode(String,XNode,Class$<$?$>$,LanguageDriver,String&#41;](https://github.com/mybatis/mybatis-3/blob/mybatis-3.4.6/src/main/java/org/apache/ibatis/builder/xml/XMLStatementBuilder.java#L134)

- spark: [spark.staticfiles.StaticFilesConfiguration.configureExternal(String&#41;](https://github.com/perwendel/spark/blob/2.7.2/src/main/java/spark/staticfiles/StaticFilesConfiguration.java#L161)

- jcodec: [org.jcodec.codecs.h264.decode.BlockInterpolator.getChromaXXUnsafe(byte[],int,int,byte[],int,int,int,int,int,int,int,int&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/h264/decode/BlockInterpolator.java#L890)

- mybatis-3: [org.apache.ibatis.executor.resultset.ResultSetWrapper.loadMappedAndUnmappedColumnNames(ResultMap,String&#41;](https://github.com/mybatis/mybatis-3/blob/mybatis-3.4.6/src/main/java/org/apache/ibatis/executor/resultset/ResultSetWrapper.java#L140)

- junit4: [org.junit.experimental.categories.CategoryFilterFactory.parseCategories(String&#41;](https://github.com/junit-team/junit4/blob/r4.13-beta-2/src/main/java/org/junit/experimental/categories/CategoryFilterFactory.java#L36)

- junit4: [org.junit.internal.TextListener.printFooter(Result&#41;](https://github.com/junit-team/junit4/blob/r4.13-beta-2/src/main/java/org/junit/internal/TextListener.java#L80)

- jcodec: [org.jcodec.codecs.h264.decode.BlockInterpolator.getChromaX0Unsafe(byte[],int,int,byte[],int,int,int,int,int,int,int&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/h264/decode/BlockInterpolator.java#L847)

- jcodec: [org.jcodec.containers.mps.MPSUtils.mpeg2Pes(int,int,int,ByteBuffer,long&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/containers/mps/MPSUtils.java#L197)

- jcodec: [org.jcodec.codecs.mpeg4.MPEG4Interpolator.vertMiddle8Safe(byte[],int,byte[],int,int,int,int&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/mpeg4/MPEG4Interpolator.java#L464)

- jcodec: [org.jcodec.codecs.h264.decode.BlockInterpolator.getLuma00Unsafe(byte[],int,int,byte[],int,int,int,int,int,int&#41;](https://github.com/jcodec/jcodec/blob/v0.2.3/src/main/java/org/jcodec/codecs/h264/decode/BlockInterpolator.java#L100)
