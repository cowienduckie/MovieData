using System.Collections.Generic;

namespace MovieData.Client.Models
{
    public class ActorData
    {
        public string Name { get; set; }
        public decimal PointVote { get; set; }
        public int MovieCount { get; set; }
    }

    public class ActorWrapper
    {
        public List<ActorData> Data { get; set; }
    }
}
