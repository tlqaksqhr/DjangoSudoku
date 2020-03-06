elapsed_time = 0;

timer = setInterval(function(){
    elapsed_time+=1;

    let timer_textbox = document.querySelector("#timer-box > h3");

    let seconds = parseInt(elapsed_time%60);
    let minutes = parseInt((elapsed_time%3600)/60);
    let hours = parseInt(elapsed_time/3600);

    seconds = seconds.toString().padStart(2, '0');
    minutes = minutes.toString().padStart(2, '0');
    hours = hours.toString().padStart(2, '0');

    timer_textbox.innerText = `${hours}:${minutes}:${seconds}`;

},1000);

function init(){

        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFToken"
        axios.defaults.headers.common['X-CSRFToken'] = getCookie("csrftoken");

        axios.get('/sudoku/make')
            .then(make_sudoku);

        $('#success-toast-container').hide();
        $('#fail-toast-container').hide();

        
        let button_flexbox = document.querySelector("#submit-btn");
        let ranking_button = document.querySelector("#ranking_submit");

        button_flexbox.addEventListener("click",function(){
            axios.post('/sudoku/check',
                get_sudoku_data()
            ).then(process_result);
        });

        ranking_button.addEventListener("click", function(){
            let name = document.querySelector("#ranking_username_textbox").value;
            submit_ranking(name);
        });
}



function get_sudoku_data() {
    let data = {
        'elapsed_time':elapsed_time,
    }

    let grid_container = document.querySelector(".gridbox-container");
    let board = [];

    for(let i=0;i<9;i++){
        for(let j=0;j<9;j++){
            let k = i*9 + j;
            let cell = grid_container.children[k];
            if(k%9==0){ 
                board.push([]);
            }
            board[i].push(Number(cell.innerText));
        }
    }

    data['puzzle'] = board;
    
    return data;
}

function process_result(response) {
    let status = response.data.status;
    clearInterval(timer);

    if(status == 'clear'){
        $('#success-toast-container').show();
        $('#success-toast').toast('show');
        
    }else{
        $('#fail-toast-container').show();
        $('#fail-toast').toast('show');
    }
}

function submit_ranking(name){
    axios.post("/sudoku/ranking/register",{
        'name' : name
    }).then(function(response){
        let status = response.data;
        if(status == 'success'){
            location.href = "/ranking";
        }
        $('#success-toast-container').hide();
    });
}

function make_sudoku(response){
    let board = response.data.board;
    let grid_container = document.querySelector(".gridbox-container");
    for(let i=0;i<9;i++){
        for(let j=0;j<9;j++){
            let node = document.createElement("div");
            node.classList.add("gridbox-item")

            if(i!=0 && i%3==2)
                node.classList.add("cell-padding-bottom");
            
            if(j!=0 && j%3==0)
                node.classList.add("cell-padding-left");

            if(board[i][j]==0){      
                node.contentEditable = true;
                node.innerText = "";
                node.classList.add("input-item-decorator");
            }else{
                node.innerText = board[i][j].toString();
                node.classList.add("fixed-item-decorator");
            }
            grid_container.appendChild(node);
        }
    }
}

function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}