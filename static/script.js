// Randomly display images
$(document).ready(function() {
    var container = $("#image-container");
    var cards = container.find(".card").toArray();
    shuffleArray(cards);
    container.empty().append(cards);
});

function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}


// AJAX filter images by checked boxes (form-switches)

//listen for one or more checkboxes to be checked from filter.html
$(document).ready(function() {
    $('.tag-checkbox').change(function() {
        // Call a function to update images when checkboxes change
        updateImages();
    });
});

//whichever tag or tags are "selected", display only images in images.html which have matching tags
function updateImages() {
    // Gather selected tag IDs
    var selectedTags = $('.tag-checkbox:checked').map(function() {
        return $(this).val();
    }).get();

    // If no tags are selected, show all images
    if (selectedTags.length === 0) {
        $('.card').show(); // Show all images
        return; // Exit the function
    }

    // Send selected tag IDs to the server using AJAX
    $.ajax({
        type: 'POST',
        url: '/filter_images',
        data: { tags: selectedTags },
        success: function(response) {
            // Update images based on filtered response
            $('.card').hide();
            $.each(response.images, function(index, imageName) {
                $('img[data-tags*="' + imageName + '"]').closest('.card').show();
            });
        }
    });
}


//if all switches unselected, display all totoros
