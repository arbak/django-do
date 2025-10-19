// Main JavaScript file for the Django app

function showAlert() {
    alert('JavaScript is working! Static files are properly configured.');
}

// Add some interactive functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log('Django app loaded successfully!');
    
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
