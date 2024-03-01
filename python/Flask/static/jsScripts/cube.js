const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight - 57);
renderer.setPixelRatio(devicePixelRatio);

const ambientlight1 = new THREE.AmbientLight(0xFFFFFF, 1);
scene.add(ambientlight1);

const plightside1 = new THREE.PointLight(0xFFFFFF, 1.2);
plightside1.position.set(0, 5, 0);
scene.add(plightside1);

document.body.appendChild(renderer.domElement);

var geometry = new THREE.BoxGeometry();
for (var i = 0; i < geometry.faces.length; i++) {
    geometry.faces[i].color.setHex(Math.random() * 0xffffff);
}
var material = new THREE.MeshBasicMaterial({ color: 0xffffff, vertexColors: true });
var cube = new THREE.Mesh(geometry, material);
scene.add(cube);

function random_rgba() {
    var o = Math.round, r = Math.random, s = 255;
    return 'rgb(' + o(r() * s) + ',' + o(r() * s) + ',' + o(r() * s) + ')';
}


var cubepos = null;
var cubespeed = null;
var cubeacceleration = null;
var camera_zoom = null;
var substance_density_text = null;
var cubespeed2 = 0;

var substance_density = 0.003;

camera.position.z = 5;
var bgcolor = random_rgba();
scene.background = new THREE.Color(bgcolor);

window.addEventListener("resize", function () {
    var width = window.innerWidth;
    var height = window.innerHeight;
    renderer.setSize(width, height);
    camera.aspect = width / height;
    camera.updateProjectionMatrix;
});

var canvas = document.getElementById('myCanvas');
canvas.width = 300;
canvas.height = 200;
canvas.style.left = "5px";
canvas.style.bottom = "10px";
canvas.style.position = "absolute";
var ctx = canvas.getContext('2d');
ctx.font = '24px Arial';
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';
ctx.fillStyle = 'black';
ctx.fillText('Reset - [r]', 70, 30);
ctx.fillText('Pause(freeze) - [f]', 113, 10);
ctx.fillText('Move - [w] [a] [s] [d]', 120, 50);
ctx.fillText('Zoom - [Mouse wheel]', 130, 80);

var x_speed = 0;
var y_speed = 0;
var x_acceleration = 0;
var y_acceleration = 0;

window.addEventListener("keydown", function (event) {
    if (event.key == "w") {
        y_acceleration = 0.01;
        return;
    }
    if (event.key == "s") {
        y_acceleration = -0.01;
        return;
    }
    if (event.key == "a") {
        x_acceleration = -0.01;
        return;
    }
    if (event.key == "d") {
        x_acceleration = 0.01;
        return;
    }
    if (event.key == "r") { //reset func
        //reset pos
        cube.position.x = 0;
        cube.position.y = 0;
        //reset acceleration
        x_acceleration = 0;
        y_acceleration = 0;
        //reset rotation
        cube.rotation.x = Math.PI / 180 * 90;
        cube.rotation.y = Math.PI / 180 * 90;
        cube.rotation.z = Math.PI / 180 * 90;
        //reset speed
        x_speed = 0;
        y_speed = 0;
        //pick random background color
        bgcolor = random_rgba();
        console.log("New scene color setted:" + bgcolor);
        scene.background = new THREE.Color(bgcolor);
        //pick random cube colors
        scene.remove(cube);
        geometry = new THREE.BoxGeometry();
        for (var i = 0; i < geometry.faces.length; i++) {
            geometry.faces[i].color.setHex(Math.random() * 0xffffff);
            console.log("Setted new color for one cube");
        }
        material = new THREE.MeshBasicMaterial({ color: 0xffffff, vertexColors: true });
        cube = new THREE.Mesh(geometry, material);
        scene.add(cube);
        //reset camera position
        camera.position.z = 5;

    }
    if (event.key == "f") {
        x_speed = 0;
        y_speed = 0;
        x_acceleration = 0;
        y_acceleration = 0;
        return;
    }

});

window.addEventListener("keyup", function (event) {
    if (event.key == "w" || event.key == "s") {
        y_acceleration = 0;
        return;
    }
    if (event.key == "a" || event.key == "d") {
        x_acceleration = 0;
        return;
    }
});

window.addEventListener("wheel", function (event) {
    if (event.deltaY > 0) {
        camera.position.z += 1;
    }
    else {
        camera.position.z -= 1;
    }
});

var canvasDynamic = document.getElementById('DynamicCanvas');
canvasDynamic.width = 500;
canvasDynamic.height = 200;
canvasDynamic.style.right = "5px";
canvasDynamic.style.bottom = "10px";
canvasDynamic.style.position = "absolute";
var ctxDynamic = canvasDynamic.getContext('2d');

function animate() {
    requestAnimationFrame(animate);
    cubespeed2 = Math.sqrt(Math.pow(x_speed, 2) + Math.pow(y_speed, 2)).toFixed(3);
    //rotation
    cube.rotation.x += x_speed;
    cube.rotation.y += y_speed;
    cube.rotation.z += x_speed + y_speed;
    //air resistance 
    if (x_acceleration == 0 && x_speed != 0) {
        if (x_speed < substance_density + 0.001 && x_speed > - (substance_density + 0.001) ) {
            x_speed = 0;
        }
        else {
            if (x_speed > 0) {
                x_speed -= substance_density;
            }
            else {
                x_speed += substance_density;
            }
        }
    }
    if (y_acceleration == 0 && y_speed != 0) {
        if (y_speed < substance_density + 0.001 && y_speed > - (substance_density + 0.001) ) {
            y_speed = 0;
        }
        else {
            if (y_speed > 0) {
                y_speed -= substance_density;
            }
            else {
                y_speed += substance_density;
            }
        }
    }
    //speed and acceleration
    x_speed += x_acceleration;
    y_speed += y_acceleration;

    cube.position.x += x_speed;
    cube.position.y += y_speed;

    //updating canvas 
    ctxDynamic.clearRect(0, 0, canvasDynamic.width, canvasDynamic.height);
    ctxDynamic.font = '24px Arial';
    ctxDynamic.textAlign = 'center';
    ctxDynamic.textBaseline = 'middle';
    ctxDynamic.fillStyle = 'black';

    cubepos = "Cube position: [X]:" + cube.position.x.toFixed(2) + ", [Y]:" + cube.position.y.toFixed(2);
    cubespeed = "Cube speed: " + (Math.sqrt(Math.pow(x_speed, 2) + Math.pow(y_speed, 2))).toFixed(3);
    cubeacceleration = "Cube acceleration:" + (Math.sqrt(Math.pow(x_acceleration, 2) + Math.pow(y_acceleration, 2))).toFixed(5);
    camera_zoom = "Camera zoom:" + camera.position.z;
    substance_density_text = "Substance density:"+ substance_density;

    ctxDynamic.fillText(cubepos, 270, 50);
    ctxDynamic.fillText(cubespeed, 200, 80);
    ctxDynamic.fillText(cubeacceleration, 260, 110);
    ctxDynamic.fillText(camera_zoom, 200, 140);
    ctxDynamic.fillText(substance_density_text, 230, 20);


    renderer.render(scene, camera);
}
animate();