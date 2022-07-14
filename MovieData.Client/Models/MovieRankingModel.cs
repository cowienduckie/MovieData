using System.Collections.Generic;

namespace MovieData.Client.Models
{
    public class MovieRankingModel
    {
        public MapData CountryInfo { get; set; }
        public List<FilmData> RegionData { get; set; }
        public List<FilmData> AllData { get; set; }
    }
}
