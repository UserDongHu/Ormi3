async function promise(){
    let a = 1 + 1;
    if (a == 3){
        return 'success';
    } else {
        throw new Error('failed');
    }
}