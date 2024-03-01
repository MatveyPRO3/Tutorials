import { OrbitControls } from "https://threejs.org/examples/jsm/controls/OrbitControls.js";

var scene = new THREE.Scene();

var camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.z = 15;

var renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
renderer.setClearColor(0x000000, 0);
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.domElement.setAttribute("id", "Cup3DObj");

document.body.appendChild(renderer.domElement);

const ambientlight1 = new THREE.AmbientLight(0xffffff, 1);
scene.add(ambientlight1);

var plightside1 = new THREE.PointLight(0xffffff, 1.2);
plightside1.position.set(0, 0, 5);
scene.add(plightside1);

var plightside2 = new THREE.PointLight(0xffffff, 1.2);
plightside2.position.set(0, 0, -5);
scene.add(plightside2);

var plightroof1 = new THREE.PointLight(0xffffff, 1.2);
plightroof1.position.set(0, 5, 0);
scene.add(plightroof1);

var plightbottom = new THREE.PointLight(0xffffff, 1.2);
plightbottom.position.set(0, -5, 0);
scene.add(plightbottom);

var plightside3 = new THREE.PointLight(0xffffff, 1.2);
plightside3.position.set(5, 0, 0);
scene.add(plightside3);

// const helperforside1 = new THREE.PointLightHelper(plightside1);
// scene.add(helperforside1);
// const helperforside3 = new THREE.PointLightHelper(plightside3);
// scene.add(helperforside3);
// const helperbottom = new THREE.PointLightHelper(plightbottom);
// scene.add(helperbottom);
// const helperforside2 = new THREE.PointLightHelper(plightside2);
// scene.add(helperforside2);
// const helperforroof1 = new THREE.PointLightHelper(plightroof1);
// scene.add(helperforroof1);

scene.background = new THREE.Color(0x00a674);

let loader = new THREE.GLTFLoader();
let obj = null;

loader.load("/static/3D/scene.gltf", function (gltf) {
  obj = gltf;
  obj.scene.scale.set(1.3, 1.3, 1.3);
  scene.add(obj.scene);
});

window.addEventListener("resize", function () {
  var width = window.innerWidth;
  var height = window.innerHeight;
  renderer.setSize(width, height);
  camera.aspect = width / height;
  camera.updateProjectionMatrix;
});
var controls = new OrbitControls(camera, renderer.domElement);
controls.autoRotate = true;
controls.autoRotateSpeed = 20;
controls.update();

var val = 0.00000001;

function animate() {
  requestAnimationFrame(animate);
  if (obj) {
    // obj.scene.rotation.y += 0.3;
  }
  controls.update();
  val = val += 0.02;
  renderer.render(scene, camera);
}

animate();
