import AssemblyKeys._

assemblySettings

name := "template-scala-parallel-recommendation"

organization := "com.appchoose"

val pioVersion = "0.12.0-incubating"

libraryDependencies ++= Seq(
  "org.apache.predictionio" %% "apache-predictionio-core" % pioVersion % "provided",
  "org.apache.spark" %% "spark-core" % "2.1.1" % "provided",
  "org.apache.spark" %% "spark-mllib" % "2.1.1" % "provided",
  "edu.stanford.nlp" % "stanford-corenlp" % "3.8.0")
