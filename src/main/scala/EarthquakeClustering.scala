import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.feature.{PCA, StandardScaler, VectorAssembler}
import org.apache.spark.sql.SparkSession

object EarthquakeClustering {
  def main(args: Array[String]): Unit = {
    // 初始化 Spark
    val spark = SparkSession.builder.appName("EarthquakeClustering").getOrCreate()

    // 从 CSV 文件读取数据
    val data = spark.read
      .option("header", "true")
      .option("inferSchema", "true")
      .csv("D:\\earthquake\\src\\main\\resources\\earthquake.csv")

    // 数据预处理
    val assembler = new VectorAssembler()
      .setInputCols(Array("latitude", "longitude"))
      .setOutputCol("features")

    val featureData = assembler.transform(data)

    val scaler = new StandardScaler()
      .setInputCol("features")
      .setOutputCol("scaledFeatures")
      .setWithMean(true)
      .setWithStd(true)

    val scalerModel = scaler.fit(featureData)
    val scaledData = scalerModel.transform(featureData)

    // 特征降维
    val pca = new PCA()
      .setInputCol("scaledFeatures")
      .setOutputCol("pcaFeatures")
      .setK(2)  // 设置目标降维的维度

    val pcaModel = pca.fit(scaledData)
    val pcaData = pcaModel.transform(scaledData)

    // 迭代收敛
    val kmeans = new KMeans()
      .setK(3)
      .setSeed(1L)
      .setMaxIter(20)  // 设置最大迭代次数
      .setTol(1e-4)  // 设置收敛阈值

    val model = kmeans.fit(pcaData)

    // 预测
    val predictions = model.transform(pcaData)

    // 展示结果
    predictions.show()

    // 停止 Spark
    spark.stop()
  }
}
