using System;
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

        [HttpGet]
        [Route("Map")]
        public IActionResult Index()
        {
            var model = _movieRepo.GetMap();

            return View(model);
        }

        [HttpGet]
        [Route("Map/Detail/{countryCode}")]
        public IActionResult Detail(string countryCode)
        {
            countryCode = countryCode.ToUpper();

            var model = _movieRepo.GetDetailModel(countryCode);

            return View(model);
        }
    }
}
