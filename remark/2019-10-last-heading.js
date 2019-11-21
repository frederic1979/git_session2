// Browse each slides to find the last heading to add a margin
slides = document.getElementsByClassName('remark-slide-content');

for (const slide of slides) {
  headings = slide.querySelectorAll("h1, h2, h3, h4, h5, h6")
  headings[headings.length - 1].classList.add('last-heading')
}
