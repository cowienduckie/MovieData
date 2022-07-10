using System.Collections.Generic;

namespace MovieData.Client.Models
{
    public class FilmWrapper
    {
        public FilmContainer Data;
    }

    public class FilmContainer
    {
        public List<FilmData> Region;
        public List<FilmData> All;
    }
}
