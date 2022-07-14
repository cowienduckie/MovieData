using System.Collections.Generic;

namespace MovieData.Client.Models
{
    public class DetailModel
    {
        public MapData CountryInfo { get; set; }
        public List<HistogramChartData> HistogramChartData { get; set; }
        public LineChartContainer LineChartData { get; set; }
        public List<PieChartData> PieChartData { get; set; }
        public PyramidChartWrapper PyramidChartData { get; set; }
        public HeatChartWrapper HeatChartData { get; set; }
    }
}