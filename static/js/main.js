const testims = document.querySelectorAll('.testim-card');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');

let currenttestimIndex = 0;

async function loadTestimonials() {
  const response = await fetch("./static/js/testimonials.json");
  const testimonials = await response.json();
  return testimonials;
}

loadTestimonials().then(testimonials => {
  document.querySelector(".testim-text").innerHTML = testimonials[currenttestimIndex].text;

  prevButton.addEventListener('click', () => {
      currenttestimIndex = (currenttestimIndex - 1 + testimonials.length) % textList.length;
      document.querySelector(".testim-text").innerHTML = testimonials[currenttestimIndex].text;
      document.querySelector(".testim-author").innerHTML = testimonials[currenttestimIndex].author;
  });
  
  nextButton.addEventListener('click', () => {
      currenttestimIndex = (currenttestimIndex + 1) % testimonials.length;
      document.querySelector(".testim-text").innerHTML = testimonials[currenttestimIndex].text;
      document.querySelector(".testim-author").innerHTML = testimonials[currenttestimIndex].author;
  });
});  

