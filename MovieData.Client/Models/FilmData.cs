using System;
using System.Collections.Generic;

namespace MovieData.Client.Models
{
    public class FilmData
    {
        public string Id { get; set; }
        public int Budget { get; set; }
        public string Title { get; set; }
        public string Overview { get; set; }
        public decimal Popularity { get; set; }
        public decimal VoteAverage { get; set; }
        public DateTime Date { get; set; }
        public List<Country> Country { get; set; }
    }
}
