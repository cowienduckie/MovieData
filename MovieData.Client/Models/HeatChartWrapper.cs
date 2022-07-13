using System.Collections.Generic;

namespace MovieData.Client.Models
{
    public class HeatChartWrapper
    {
        public int Max { get; set; }
        public int Min { get; set; }
        public List<HeatChartContainer> Region { get; set; }
        public List<HeatChartContainer> All { get; set; }
    }

    public class HeatChartContainer
    {
        public string Name { get; set; }
        public List<HeatChartData> Data { get; set; }
    }
}