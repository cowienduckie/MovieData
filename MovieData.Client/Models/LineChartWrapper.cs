using System.Collections.Generic;

namespace MovieData.Client.Models
{
    public class LineChartWrapper
    {
        public List<LineChartContainer> Data;
    }

    public class LineChartContainer
    {
        public List<LineChartData> Region;
        public List<LineChartData> All;
    }
}