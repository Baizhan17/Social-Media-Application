<template>
  <div ref="BgContainer" class="absolute inset-0"></div>
</template>

<script>
import * as THREE from 'three';

export default {
  
  mounted() {
    this.initThree();
    window.addEventListener('resize', this.onWindowResize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onWindowResize);
  },
  methods: {
    initThree() {
      const container = this.$refs.threeContainer;

      // Scene, Camera, and Renderer setup
      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
      this.renderer = new THREE.WebGLRenderer({ antialias: true });
      this.renderer.setSize(container.clientWidth, container.clientHeight);
      container.appendChild(this.renderer.domElement);

      // Basic cube geometry for demo purposes
      const geometry = new THREE.BoxGeometry();
      const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
      this.cube = new THREE.Mesh(geometry, material);
      this.scene.add(this.cube);

      // Camera position
      this.camera.position.z = 5;

      this.animate();
    },
    animate() {
      requestAnimationFrame(this.animate);
      this.cube.rotation.x += 0.01;
      this.cube.rotation.y += 0.01;
      this.renderer.render(this.scene, this.camera);
    },
    onWindowResize() {
      const container = this.$refs.threeContainer;
      this.camera.aspect = container.clientWidth / container.clientHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(container.clientWidth, container.clientHeight);
    }
  }
};
</script>

<style scoped>
.three-container {
  width: 100%;
  height: 100vh; /* Full viewport height */
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1; /* Ensure it stays in the background */
  overflow: hidden;
}
</style>
