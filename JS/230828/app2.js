const mainContainer = document.getElementById("main"); // 메인컨테이너
const BASE_URL = "https://test.api.weniv.co.kr/" // baseurl

async function getjson() { // json을 받아오는 함수
    try { // try catch문으로 예외처리
        const res = await fetch(BASE_URL + 'mall'); // await 사용으로 res을 받아올때까지 기다림
        const resjson = await res.json(); //  await으로 res의 json을 반환할때까지 기다림.
        return resjson; // async함수는 promise객체로 반환
    }
    catch (error) {
        console.log(error); // 에러 발생시
    }
}

function createProduct(imgUrl, productId, productName, productPrice, onClick){ // 상품의 사진과 id, Name, Price, onclick 함수를 인자로 받음
    const $product = document.createElement("div"); // 상품을 표시할 div요소 생성

    const $productName = document.createElement("strong"); // 이름을 표시할 strong요소 생성
    const $productPrice = document.createElement("span"); // 가격을 표시할 span요소 생성
    const $imgUrl = document.createElement("img"); // 상품의 이미지를 표시할 img요소 생성
    const $br = document.createElement("br"); // 상품의 사진과 정보를 줄 구분할 br요소 생성

    $productName.innerText = productId + ". " + productName; // strong요소에 상품id와 상품이름 추가
    $productPrice.innerText = " / "+ productPrice + "원"; // span요소에 가격 정보 추가
    $imgUrl.src = imgUrl; // img요소 src에 받아온 imgUrl 설정

    $product.append($imgUrl, $br, $productName, $productPrice); // div요소에 이미지, br, 상품 이름, 상품 가격 추가.
    $product.addEventListener("click", onClick) // 상품 div요소를 클릭했을때의 함수 onClick을 호출하는 이벤트 리스너 추 가

    return $product; // 상품 div요소를 리턴


}

async function writehtml() { // 받아온 json으로 html 작성하는 메인 함수
    const productsContainer = document.createElement("div"); // 상품들을 배치할 상품 컨테이너 div요소 생성
    const detailContainer = document.createElement("div"); // 상품의 상세사진을 넣을 detail 컨테이너 div요소 생성
    detailContainer.id = "detail"; // detailContainer에 id값 추가
    mainContainer.append(productsContainer, detailContainer); // 메인컨테이너에 상품 컨테이너와 상세사진 컨테이너 추가

    const data = await getjson(); // await로 getjson함수에서 data를 반환할때가지 기다림.
    data.forEach(data => { // 받아온 data는 json객체 형태이므로 foreach메소드를 사용해서 각각의 요소들 data에 접근
        const productId = data.id; // 상품의 id
        const productName = data.productName; // 상품의 이름
        const productPrice = data.price; // 상품의 가격
        const imgUrl = BASE_URL + data.thumbnailImg; // 상품의 이미지 주소
        function onClick(e){ // 상품을 클릭했을때 호출될 onclick함수
            detailContainer.innerHTML = ""; // 클릭하면 상세사진 컨테이너를 초기화
            data.detailInfoImage.forEach(detaildata=>{ // 각 상세사진들의 주소들을 foreach메소드를 이용해서 detaildata로 받아와서 접근
                const detailImgUrl = BASE_URL + detaildata; // 상세사진 주소
                const $productDetail = document.createElement("img"); // 상세사진을 담을 img요소를 생성
                $productDetail.src = detailImgUrl; // img요소의 src를 설정
                detailContainer.append($productDetail); // 상세사진 컨테이너에 img요소 추가
            })
            detailContainer.scrollIntoView({behavior: "smooth"}); // 상품 컨테이너를 눌렀을 때, 상세사진 컨테이너로 스크롤을 smooth하게 내림
        }

        const product = createProduct(imgUrl, productId, productName, productPrice, onClick); // createProduct함수에 data로 가져온 인자들을 넣어 div요소를 반환해 상품 생성
        productsContainer.appendChild(product); // 상품 컨테이너에 반환된 div 상품을 추가
    });
}
writehtml(); // 메인함수 호출