<template>
  <div class="login">
    <div v-if="!isLogin">
      <input type="text" placeholder="username" v-model="username" />
      <input type="password" placeholder="password" v-model="password" />
      <button @click="sendLogin">
        Login
      </button>
    </div>
  </div>
</template>

<script>
import MixinUsersApi from "@/mixins/UsersApi.js";

export default {
  name: "HelloWorld",
  mixins: [MixinUsersApi],
  props: {},
  data() {
    return {};
  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
