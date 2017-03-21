$(document).ready(function(){
    showTranslator();

    function showWords() {
        $(".translate-btn").removeClass("active-btn");
        $(".add-words-btn").addClass("active-btn");
        $(".input-block").empty();
        $(".input-block").html(
            "<input type='text' class='u-full-width word-input' placeholder='Add a word to your vocabulary' />"
            + "<button id='submit-word' class='button-primary'>Submit Word</button>"
        );

        $("#submit-word").click(function(){
            var wordValue = $(".word-input").val();
            if (wordValue) {
                $(".warning-block").html("");
                $.post("/save_word", {"word" :wordValue}, function(response){
                    var new_word = JSON.parse(response).new_word
                    $(".warning-block").html(
                        "<span class='material-icons success-icon'>done</span><h3>"+ new_word +"</h3>");
                });
            }
            else {
                $(".warning-block").html("");
                $(".warning-block").html("Please, enter word first");
            }
        });
    };

    function showTranslator() {
        $(".add-words-btn").removeClass("active-btn");
        $(".translate-btn").addClass("active-btn");
        $(".input-block").empty();
        $(".input-block").html(
            "<textarea id='translate-textarea' class='u-full-width' placeholder='What do you want to translate?'></textarea>"
            + "<button id='submit-translate' class='button-primary'>Translate</button>"
        );
        $("#submit-translate").click(function(){
            var translateValue = $("#translate-textarea").val();
            if (translateValue) {
                $(".warning-block").html("");
                /*$.post("https://translate.yandex.net/api/v1.5/tr/translate?key=trnsl.1.1.20170316T202440Z.22bfa4c621f0ef70.41db300301a93317a65f0f43d0da8e2b81ab3d73&text="+ translateValue +"&lang=en-ru&format=plain&options=1", function(response){
                    $(".warning-block").html("<span class='material-icons success-icon'>done</span>");
                    console.log(response);
                });*/
            }
            else {
                $(".warning-block").html("");
                $(".warning-block").html("Please, enter word to translate first");
            }
        });
    };

    $(".add-words-btn").click(function(){
        showWords();
    });

    $(".translate-btn").click(function(){
        showTranslator()
    });
});