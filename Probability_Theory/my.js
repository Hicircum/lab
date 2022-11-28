function saveValue() {
    var valueN = document.getElementById("floatingN").value;
    var valueP = document.getElementById("floatingP").value;
    // document.getElementById("floatingID").value = "";
    // document.getElementById("floatingPassword").value = "";
    n = parseFloat(valueN);
    p = parseFloat(valueP);
    console.log(n,p);
    Init(n,p);
}

function valueget(){
    var valueN = document.getElementById("Rangen").value;
    var valueP = document.getElementById("Rangep").value;
    document.getElementById("adn").innerHTML="调节n="+valueN;
    document.getElementById("adp").innerHTML="调节p="+valueP;
    n = parseFloat(valueN);
    p = parseFloat(valueP);
    Init(n,p);
}

function ValueAdjust() {
    var valueN = document.getElementById("floatingN").value;
    var valueP = document.getElementById("floatingP").value;
    // document.getElementById("floatingID").value = "";
    // document.getElementById("floatingPassword").value = "";
    n = parseFloat(valueN);
    p = parseFloat(valueP);
    console.log(n,p);
    Init(n,p);
}

function factorial(n) {
    var jc=1;
    if(n<=1){
        return jc;
    }else{
        jc=n*arguments.callee(n-1);
    }
    return jc;
}

function C(n,k) {
    a = factorial(n);
    return a/(factorial(k)*factorial(n-k));
}


function getColor() {
    let color = [];
    var BDc = document.getElementById("Binomial_Distribution_color").value;
    var PDc = document.getElementById("Poisson_distribution_color").value;
    var NDc = document.getElementById("Normal_distribution_color").value;
    color.push(BDc);
    color.push(PDc);
    color.push(NDc);
    return color;
}

function getSmooth() {
    var smooth = document.getElementById("issmooth").checked;
    if (smooth) {
        return 0.3
    } else {
        return false
    }
}

function getYmax() {
    var ym = parseFloat(document.getElementById("data-zoom-y").value);
    return ym;
}

// 二项分布
function Binomial_Distribution_Y(n,p,k) {
    x = C(n,k)*Math.pow(p,k);
    x2 = Math.pow((1-p),(n-k));
    return x*x2;
}


function Binomial_Distribution(n,p) {
    let data = [];
    for (let i = -100; i <= 150; i += 1) {
        data.push([i, Binomial_Distribution_Y(n,p,i)]);
    }
    return data;
}


//泊松分布
function Poisson_distribution_Y(ld,k) {
    return Math.pow(ld,k)/factorial(k)*Math.pow(Math.E,-ld);
}

function Poisson_distribution(ld) {
    let data = [];
    for (let i = -100; i <= 150; i += 1) {
        data.push([i, Poisson_distribution_Y(ld,i)]);
    }
    return data;
}


// 正态分布
function Normal_distribution_Y(a,b,x) {
    ax = 1/b/Math.pow(2*Math.PI,0.5);
    bx = Math.pow(x - a,2)/2/Math.pow(b,2);
    return ax * Math.exp(-bx);
}

function Normal_distribution(a,b) {
    let data = [];
    for (let i = -100; i <= 150; i += 1) {
        data.push([i, Normal_distribution_Y(a,b,i)]);
    }
    return data;
}


// 图表部分
var dom = document.getElementById('chart');
var myChart = echarts.init(dom, null, {
    renderer: 'canvas',
    useDirtyRect: false
});
var app = {};
var option;

function Init(n,p) {
    option = {
        title: {
            text: '曲线对比'
        },
        tooltip: {
            trigger: 'axis'
        },
        color: getColor(),
        animation: false,
        grid: {
            top: 40,
            left: 50,
            right: 40,
            bottom: 50
        },
        legend: {
            data: ['二项分布', '泊松分布', '正态分布']
        },
        toolbox: {
            feature: {
              saveAsImage: {}
            }
        },
        xAxis: {
            name: 'k',
            min: -110,
            max: 110,
            minorTick: {
                show: true
            },
            minorSplitLine: {
                show: true
            }
        },
        yAxis: {
            name: 'p',
            min: -1,
            max: 100,
            minorTick: {
                show: true
            },
            minorSplitLine: {
                show: true
            }
        },
        dataZoom: [
            {
                show: true,
                type: 'inside',
                filterMode: 'none',
                xAxisIndex: [0],
                startValue: n*p-20,
                endValue: n*p+20
            },
            {
                show: true,
                type: 'inside',
                filterMode: 'none',
                yAxisIndex: [0],
                startValue: -0.1,
                endValue: getYmax()
            }
        ],
        series: [
            {
                name: '二项分布',
                type: 'line',
                showSymbol: false,
                clip: true,
                data: Binomial_Distribution(n,p),
                smooth: getSmooth()
            },
            {
                name: "泊松分布",
                type: 'line',
                showSymbol: false,
                clip: true,
                data: Poisson_distribution(n*p),
                smooth: getSmooth()
            },
            {
                name: "正态分布",
                type: 'line',
                showSymbol: false,
                clip: true,
                data: Normal_distribution(n*p,Math.pow((n*p*(1-p)),0.5)),
                smooth: getSmooth()
            }
        ]
    };
    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }
}
window.addEventListener('resize', myChart.resize);

Init(30,0.1);
