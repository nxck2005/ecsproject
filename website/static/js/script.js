// Smooth scrolling for navbar links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Fade-in effect for elements when page loads
window.addEventListener('load', () => {
    document.querySelectorAll('.fade-in').forEach(element => {
        element.style.opacity = '0';
        element.style.transition = 'opacity 1.5s ease-in-out';
        setTimeout(() => element.style.opacity = '1', 200);
    });
});

// Back-to-Top button functionality
const backToTopBtn = document.createElement('button');
backToTopBtn.innerText = '↑ Top';
backToTopBtn.id = 'back-to-top';
backToTopBtn.style.position = 'fixed';
backToTopBtn.style.bottom = '20px';
backToTopBtn.style.right = '20px';
backToTopBtn.style.padding = '10px 15px';
backToTopBtn.style.fontSize = '18px';
backToTopBtn.style.display = 'none';
backToTopBtn.style.backgroundColor = '#3498db';
backToTopBtn.style.color = '#fff';
backToTopBtn.style.border = 'none';
backToTopBtn.style.borderRadius = '5px';
backToTopBtn.style.cursor = 'pointer';
document.body.appendChild(backToTopBtn);

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTopBtn.style.display = 'block';
    } else {
        backToTopBtn.style.display = 'none';
    }
});

backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
