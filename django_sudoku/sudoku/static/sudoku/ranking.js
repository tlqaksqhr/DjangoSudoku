function init(){
    axios.get('/sudoku/ranking')
    .then(get_sudoku_ranking);
}

function get_sudoku_ranking(response){
    let ranking_data = response.data.data;
    let ranking_list = document.querySelector("#ranking-list")
    let count = 1;
    ranking_data.forEach(element => {
        let tr = document.createElement("tr");
        let rankElement = document.createElement("td");
        let userElement = document.createElement("td");
        let timeElement = document.createElement("td");

        rankElement.innerText = count.toString();
        userElement.innerText = element.name;
        timeElement.innerText = element.elapsed_time;
        tr.appendChild(rankElement);
        tr.appendChild(userElement);
        tr.appendChild(timeElement);
        ranking_list.appendChild(tr);
        count += 1;
    });
}