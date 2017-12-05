package org.template.classification

import org.apache.predictionio.controller.LServing

import scala.io.Source
import org.apache.predictionio.controller.Params

case class ServingParams(filepath: String) extends Params

class Serving extends LServing[Query, PredictedResult] {

  override
  def serve(query: Query, 
            predictedResults: Seq[PredictedResult]): PredictedResult = {
    predictedResults.head
  }
}
