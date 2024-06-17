/* main/static/js/scripts.js */
document.addEventListener("DOMContentLoaded", function () {
    console.log("Document loaded and script running.");
    // Add interactivity here
  });
  // scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Function to handle feedback form submission
    var handleFeedbackForm = function() {
        var feedbackForm = document.getElementById('feedback-form');

        if (feedbackForm) {
            feedbackForm.addEventListener('submit', function(event) {
                event.preventDefault(); // Prevent default form submission

                // Optionally, provide feedback to the user
                var feedbackMessage = document.getElementById('feedback-message');
                if (feedbackMessage) {
                    feedbackMessage.textContent = 'Submitting feedback...';
                }

                // Submit the form (this will cause a full page reload)
                feedbackForm.submit();
            });
        }
    };

    // Function to handle login form submission
    var handleLoginForm = function() {
        var loginForm = document.getElementById('login-form');

        if (loginForm) {
            loginForm.addEventListener('submit', function(event) {
                event.preventDefault(); // Prevent default form submission

                // Optionally, provide feedback to the user
                var loginMessage = document.getElementById('login-message');
                if (loginMessage) {
                    loginMessage.textContent = 'Logging in...';
                }

                // Submit the form (this will cause a full page reload)
                loginForm.submit();
            });
        }
    };

    // Function to handle signup form submission
    var handleSignupForm = function() {
        var signupForm = document.getElementById('signup-form');

        if (signupForm) {
            signupForm.addEventListener('submit', function(event) {
                event.preventDefault(); // Prevent default form submission

                // Optionally, provide feedback to the user
                var signupMessage = document.getElementById('signup-message');
                if (signupMessage) {
                    signupMessage.textContent = 'Signing up...';
                }

                // Submit the form (this will cause a full page reload)
                signupForm.submit();
            });
        }
    };

    // Initialize form handlers
    handleFeedbackForm();
    handleLoginForm();
    handleSignupForm();

    // Example: Handle page transitions (e.g., fade out on link click)
    var links = document.querySelectorAll('a');

    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior

            // Optionally, perform animation or action before navigation
            document.body.classList.add('fade-out'); // Example: Add fade-out class

            // Navigate to the URL after a delay (for demo purposes)
            var href = this.getAttribute('href');
            setTimeout(function() {
                window.location.href = href;
            }, 500); // Delay in milliseconds
        });
    });
});
