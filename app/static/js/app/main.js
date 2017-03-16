$(document).ready(function(){
    $(".add-words-btn").click(function(){
        $(".input-block").html(
            "<input type='text' class='u-full-width word-input' placeholder='Add a word to your vocabulary' />"
            + "<button id='submit-word' class='button-primary'>Submit Word</button>"
        );

        $("#submit-word").click(function(){
            var wordValue = $(".word-input").val();
            if (wordValue) {
                $(".warning-block").html("");
                $.post("/save_word", {"word" :wordValue}, function(response){
                    $(".warning-block").html("<span class='material-icons success-icon'>done</span>");
                    console.log(response);
                });
            }
            else {
                $(".warning-block").html("");
                $(".warning-block").html("Please, enter word first");
            }
        });
    });
});