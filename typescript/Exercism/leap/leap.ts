function isLeapYear(ano: number) {

    const divididoPor4 = ano % 4 === 0;
    const divididoPor100 = ano % 100 === 0;
    const divididoPor400 = ano % 400 === 0;




    return divididoPor4 && !divididoPor100 || divididoPor400;


    //return  divididoPor400 || !divididoPor100 && divididoPor4;





    //return divididoPor4 && !(divididoPor400 !== divididoPor100)

    // let check = false;
    // if (ano % 4 === 0 ) {
    //     check = true;
    //     if(ano % 100 === 0 && ano % 400 === 0) {
    //         check = true
    //     } else {
    //         check = false
    //     }
    // }
    // return check

}



export default isLeapYear