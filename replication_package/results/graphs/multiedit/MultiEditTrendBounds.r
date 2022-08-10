# 23 Nov
# regenerate with shulte and statement measured only,
# separate: baselines and measure for L+S on another

library(ggplot2)

# figures below came from /home/sbr/Dropbox/Research/Gin/Medians
sizes<-seq(1,5)
measuredPassRateLine<-data.frame(size=sizes, p=c(0.05073,0.01865,0.007081,0.002804,0.001400), measure="Line")
measuredPassRateStatement<-data.frame(size=sizes, p=c(0.1498,0.1199,0.0878,0.07047,0.06237), measure="Statement")

# computed by ApplyCompileTestTimes
measuredPassRateLineNormalised<-data.frame(size=sizes, p=c(0.002,0.001111111,0.001111111,0.0,0.0), measure="Line, Normalised")

#Binomial is upper because it does not require success on last edit;  geo is
#lower because it requires failure on first 4 edits.  Compute the binomial as
#upper and geometric as lower bounds on success for 3 values of $p$:
#Extrapolating from our delete results (probability of test passing after 1 edit -> line 0.175, statement 0.345
#Schulte/Forrest's  -copy/delete/swap on C ASTs and ASM;   ASM 0.396, AST 0.339
binomialOurDeleteLine<-data.frame(size=sizes,p=dbinom(sizes,5,0.175), measure="Binomial, Del Line")
binomialOurDeleteStatement<-data.frame(size=sizes,p=dbinom(sizes,5,0.345), measure="Binomial, Del Statement")
binomialSchulteASM<-data.frame(size=sizes,p=dbinom(sizes,5,0.396), measure="Binomial, Schulte ASM")
binomialSchulteAST<-data.frame(size=sizes,p=dbinom(sizes,5,0.339), measure="Binomial, Schulte AST")

geometricOurDeleteLine<-data.frame(size=sizes,p=dgeom(sizes-1,0.175), measure="Geometric, Del Line")
geometricOurDeleteStatement<-data.frame(size=sizes,p=dgeom(sizes-1,0.345), measure="Geometric, Del Statement")
geometricSchulteASM<-data.frame(size=sizes,p=dgeom(sizes-1,0.396), measure="Geometric, Schulte ASM")
geometricSchulteAST<-data.frame(size=sizes,p=dgeom(sizes-1,0.339), measure="Geometric, Schulte AST")

#upper bound - prob of success for 1
#lower bound - power series from prob for 1
baseline1OurDeleteLine<-data.frame(size=sizes, p=0.05073^sizes, measure="Baseline 1, Line")
baseline1OurDeleteStatement<-data.frame(size=sizes, p=0.1498^sizes, measure="Baseline 1, Statement")
baseline1SchulteASM<-data.frame(size=sizes, p=0.396^sizes, measure="Baseline 1, Schulte ASM")
baseline1SchulteAST<-data.frame(size=sizes, p=0.339^sizes, measure="Baseline 1, Schulte AST")

pInd = 0.05073
baseline2OurDeleteLine<-data.frame(size=sizes, p=(1-pInd^(sizes-1))*pInd, measure="Baseline 2, Line")
baseline2OurDeleteLine[which(baseline2OurDeleteLine$size==1),"p"]=pInd
pInd = 0.1498
baseline2OurDeleteStatement<-data.frame(size=sizes, p=(1-pInd^(sizes-1))*pInd, measure="Baseline 2, Statement")
baseline2OurDeleteStatement[which(baseline2OurDeleteStatement$size==1),"p"]=pInd


allData<-data.frame()
allData<-rbind(allData,measuredPassRateLine)
allData<-rbind(allData,measuredPassRateStatement)
allData<-rbind(allData,baseline1OurDeleteLine)
allData<-rbind(allData,baseline1OurDeleteStatement)
allData<-rbind(allData,baseline1SchulteASM)
allData<-rbind(allData,baseline1SchulteAST)
allData<-rbind(allData,measuredPassRateLineNormalised)
#allData<-rbind(allData,geometricOurDeleteLine)

g<-ggplot(allData)
g<-g+geom_line(aes(x=size, y=p, color=measure, linetype=measure))
g<-g+scale_color_manual(values=c('Line'='red','Statement'='blue','Baseline 1, Line'='Red', 'Baseline 1, Statement'='Blue', 'Baseline 1, Schulte ASM'='Black', 'Baseline 1, Schulte AST'='Green', 'Line, Normalised'='Red'))#, 'Geometric, Del Line'='yellow'))
g<-g+scale_linetype_manual(values=c('Line'='solid','Statement'='solid','Baseline 1, Line'='dotted', 'Baseline 1, Statement'='dotted', 'Baseline 1, Schulte ASM'='dotdash', 'Baseline 1, Schulte AST'='dashed', 'Line, Normalised'='twodash'))#,'Geometric, Del Line'='solid'))
                                  #"twodash", "dotdash", "dotted", "dashed", "twodash", "dotdash", "dotted", "dashed", "solid", "solid"))
g<-g+labs(color = "Pass Rate", linetype = "Pass Rate", shape = "Pass Rate")
g<-g+xlab("Number of Edits")
g<-g+ylab("Success Rate")
g<-g+theme(legend.position = c(0.8,0.8))
g

# MultiEditBounds.pdf
allDataBaselines<-data.frame()
allDataBaselines<-rbind(allDataBaselines,measuredPassRateLine)
allDataBaselines<-rbind(allDataBaselines,measuredPassRateStatement)
allDataBaselines<-rbind(allDataBaselines,baseline1OurDeleteLine)
allDataBaselines<-rbind(allDataBaselines,baseline2OurDeleteLine)
allDataBaselines<-rbind(allDataBaselines,baseline1OurDeleteStatement)
allDataBaselines<-rbind(allDataBaselines,baseline2OurDeleteStatement)
allDataBaselines<-rbind(allDataBaselines,measuredPassRateLineNormalised)
g<-ggplot(allDataBaselines)
g<-g+geom_line(aes(x=size, y=p, color=measure, linetype=measure))
g<-g+scale_color_manual(values=c('Line'='red','Statement'='blue','Baseline 1, Line'='Red', 'Baseline 2, Line'='Red', 'Baseline 1, Statement'='Blue', 'Baseline 2, Statement'='Blue', 'Line, Normalised'='Red'))#, 'Geometric, Del Line'='yellow'))
g<-g+scale_linetype_manual(values=c('Line'='solid','Statement'='solid','Baseline 1, Line'='dotted', 'Baseline 2, Line'='dotdash', 'Baseline 1, Statement'='dotted', 'Baseline 2, Statement'='dotdash', 'Line, Normalised'='dashed'))#,'Geometric, Del Line'='solid'))
g<-g+labs(color = "Pass Rate", linetype = "Pass Rate", shape = "Pass Rate")
g<-g+xlab("Number of Edits")
g<-g+ylab("Pass Rate")
g<-g+theme(legend.position = c(0.8,0.7))
g

# MultiEditBoundsComparisons.pdf
allDataComparison<-data.frame()
allDataComparison<-rbind(allDataComparison,measuredPassRateStatement)
allDataComparison<-rbind(allDataComparison,baseline1SchulteASM)
allDataComparison<-rbind(allDataComparison,baseline1SchulteAST)
allDataComparison<-rbind(allDataComparison,measuredPassRateLineNormalised)
g<-ggplot(allDataComparison)
g<-g+geom_line(aes(x=size, y=p, color=measure, linetype=measure))
g<-g+scale_color_manual(values=c('Statement'='blue','Baseline 1, Schulte ASM'='Black', 'Baseline 1, Schulte AST'='Green'))#, 'Geometric, Del Line'='yellow'))
g<-g+scale_linetype_manual(values=c('Statement'='solid','Baseline 1, Schulte ASM'='dotdash', 'Baseline 1, Schulte AST'='dashed'))#,'Geometric, Del Line'='solid'))
g<-g+labs(color = "Pass Rate", linetype = "Pass Rate", shape = "Pass Rate")
g<-g+xlab("Number of Edits")
g<-g+ylab("Pass Rate")
g<-g+theme(legend.position = c(0.8,0.8))
g



########################### repairs ######################################
# RepairNoOpRates.pdf
repairFractionOfAllPasses=data.frame(Size=c(2,3,4,5,2,3,4,5),granularity=c('Line repairs/passes','Line repairs/passes','Line repairs/passes','Line repairs/passes','Statement repairs/passes','Statement repairs/passes','Statement repairs/passes','Statement repairs/passes'),rate=c(0.4180944702009,0.612534948741845,0.765212399540758,0.910227272727273,0.106497273624223,0.203444358653496,0.274109508154863,0.312671755725191))
noopRepairFractionOfAllPasses=data.frame(Size=c(2,3,4,5,2,3,4,5),granularity=c('Line no-ops/passes','Line no-ops/passes','Line no-ops/passes','Line no-ops/passes','Statement no-ops/passes','Statement no-ops/passes','Statement no-ops/passes','Statement no-ops/passes'),rate=c(0.269001776325773,0.297584818861415,0.253928866832093,0.315159574468085,0.00589614218274145,0.0163592849168846,0.0275488416782321,0.0401918296411994))
repairs<-rbind(repairFractionOfAllPasses,noopRepairFractionOfAllPasses)

g<-ggplot(repairs)
g<-g+geom_line(aes(x=Size, y=rate, color=granularity, linetype=granularity))
# g<-g+scale_color_manual(values=c('Line repairs/passes'='red','Statement repairs/passes'='blue','Line no-ops/passes'='Red', 'Statement no-ops/passes'='Blue'))
g<-g+scale_linetype_manual(values=c('Line repairs/passes'='solid','Statement repairs/passes'='solid','Line no-ops/passes'='dotted', 'Statement no-ops/passes'='dotted'))
g<-g+labs(color = "", linetype = "", shape = "")
g<-g+xlab("Number of Edits")
g<-g+ylab("Fraction of Passes")
g<-g+theme(legend.position = c(0.23,0.85))
g<-g+theme(text = element_text(size = 14))
g
