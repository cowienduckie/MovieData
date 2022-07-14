using System.Linq;
using MovieData.Client.Configs;
using MovieData.Client.Models;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using RestSharp;

namespace MovieData.Client.Repositories
{
    public interface IMovieRepository
    {
        MapWrapper GetMap();
        FilmWrapper GetFilm(string countryCode);
        LineChartWrapper GetLineChart(string countryCode);
        PieChartWrapper GetPieChart(string countryCode);
        HistogramChartWrapper GetHistogramChart(string countryCode);
        PyramidChartWrapper GetPyramidChart(string countryCode);
        HeatChartWrapper GetHeatChart(string countryCode);
        DetailModel GetDetailModel(string countryCode);
        MovieRankingModel GetMovieRanking(string countryCode);
        ActorRankingModel GetActorRanking(string countryCode);
    }

    public class MovieRepository : IMovieRepository
    {
        public MapWrapper GetMap()
        {
            var client = new RestClient($"http://{AppConfig.Host}:{AppConfig.Port}/api/map");
            var request = new RestRequest(Method.GET);
            var response = client.Execute(request);

            if (response.IsSuccessful)
            {
                var content = JsonConvert.DeserializeObject<JToken>(response.Content);

                return content.ToObject<MapWrapper>();
            }

            return null;
        }

        public FilmWrapper GetFilm(string countryCode)
        {
            var client = new RestClient($"http://{AppConfig.Host}:{AppConfig.Port}/api/film/{countryCode}");
            var request = new RestRequest(Method.GET);
            var response = client.Execute(request);

            if (response.IsSuccessful)
            {
                var content = JsonConvert.DeserializeObject<JToken>(response.Content);

                return content.ToObject<FilmWrapper>();
            }

            return null;
        }

        public LineChartWrapper GetLineChart(string countryCode)
        {
            var client = new RestClient($"http://{AppConfig.Host}:{AppConfig.Port}/api/chart/line/{countryCode}");
            var request = new RestRequest(Method.GET);
            var response = client.Execute(request);

            if (response.IsSuccessful)
            {
                var content = JsonConvert.DeserializeObject<JToken>(response.Content);

                return content.ToObject<LineChartWrapper>();
            }

            return null;
        }

        public PieChartWrapper GetPieChart(string countryCode)
        {
            var client = new RestClient($"http://{AppConfig.Host}:{AppConfig.Port}/api/chart/pie/{countryCode}");
            var request = new RestRequest(Method.GET);
            var response = client.Execute(request);

            if (response.IsSuccessful)
            {
                var content = JsonConvert.DeserializeObject<JToken>(response.Content);

                return content.ToObject<PieChartWrapper>();
            }

            return null;
        }

        public HistogramChartWrapper GetHistogramChart(string countryCode)
        {
            var client = new RestClient($"http://{AppConfig.Host}:{AppConfig.Port}/api/chart/histo/{countryCode}");
            var request = new RestRequest(Method.GET);
            var response = client.Execute(request);

            if (response.IsSuccessful)
            {
                var content = JsonConvert.DeserializeObject<JToken>(response.Content);

                return content.ToObject<HistogramChartWrapper>();
            }

            return null;
        }

        public PyramidChartWrapper GetPyramidChart(string countryCode)
        {
            var client = new RestClient($"http://{AppConfig.Host}:{AppConfig.Port}/api/chart/pyramid/{countryCode}");
            var request = new RestRequest(Method.GET);
            var response = client.Execute(request);

            if (response.IsSuccessful)
            {
                var content = JsonConvert.DeserializeObject<JToken>(response.Content);

                return content.ToObject<PyramidChartWrapper>();
            }

            return null;
        }

        public HeatChartWrapper GetHeatChart(string countryCode)
        {
            var client = new RestClient($"http://{AppConfig.Host}:{AppConfig.Port}/api/chart/heat/{countryCode}");
            var request = new RestRequest(Method.GET);
            var response = client.Execute(request);

            if (response.IsSuccessful)
            {
                var content = JsonConvert.DeserializeObject<JToken>(response.Content);

                return content.ToObject<HeatChartWrapper>();
            }

            return null;
        }

        public DetailModel GetDetailModel(string countryCode)
        {
            return new DetailModel
            {
                CountryInfo = GetMap().Data.FirstOrDefault(d => d.Code == countryCode),
                HistogramChartData = GetHistogramChart(countryCode).Data,
                LineChartData = GetLineChart(countryCode).Data,
                PieChartData = GetPieChart(countryCode).Data,
                PyramidChartData = GetPyramidChart(countryCode),
                HeatChartData = GetHeatChart(countryCode)
            };
        }

        public MovieRankingModel GetMovieRanking(string countryCode)
        {
            var filmData = GetFilm(countryCode).Data;

            return new MovieRankingModel
            {
                CountryInfo = GetMap().Data.FirstOrDefault(d => d.Code == countryCode),
                RegionData = filmData.Region,
                AllData = filmData.All
            };
        }

        public ActorRankingModel GetActorRanking(string countryCode)
        {
            return new ActorRankingModel
            {
                CountryInfo = GetMap().Data.FirstOrDefault(d => d.Code == countryCode),
                RegionData = GetFilm(countryCode).Data.Region
            };
        }
    }
}