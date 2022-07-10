using Microsoft.AspNetCore.Mvc;
using MovieData.Client.Repositories;

namespace MovieData.Client.Controllers
{
    public class MapController : Controller
    {
        private readonly IMovieRepository _movieRepo;

        public MapController(IMovieRepository movieRepo)
        {
            _movieRepo = movieRepo;
        }

        public IActionResult Index()
        {
            var model = _movieRepo.GetMap();

            return View(model);
        }

        public IActionResult Detail(string countryCode)
        {
            var model = _movieRepo.GetFilm(countryCode);

            return View(model);
        }
    }
}
