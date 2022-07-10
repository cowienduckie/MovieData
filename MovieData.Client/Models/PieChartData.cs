namespace MovieData.Client.Models
{
    public class PieChartData
    {
        public string Code { get; set; }
        public string Type { get; set; }
        public int MovieCount { get; set; }
        public decimal Popularity { get; set; }
        public int VoteCount { get; set; }
    }
}