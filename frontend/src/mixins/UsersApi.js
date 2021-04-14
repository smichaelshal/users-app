// import axios from "axios";
import SendApi from "@/mixins/SendApi.js";

export default {
  name: "UsersApi",
  mixins: [SendApi],
  data() {
    return {
      refreshToken: null,
      host: "http://localhost:8000/",
      username: "",
      password: "",
      isLogin: false,
      timeTokenAccess: 1000 * 60 * 4,
    };
  },
  methods: {
    login() {
      if (localStorage.refreshToken) {
        this.refreshToken = localStorage.refreshToken;
        this.accessToken = localStorage.accessToken;
        this.testServer();
      }
    },
    saveLogin(data) {
      this.refreshToken = data.refresh;
      this.accessToken = data.access;
      localStorage.refreshToken = data.refresh;
      localStorage.accessToken = data.refresh;
    },
    sendLogin() {
      this.sendToServer({
        url: "users/login/",
        args: {
          username: this.username,
          password: this.password,
        },
        type: "post",
        isAuth: false,
      })
        .then((data) => {
          this.isLogin = true;
          this.saveLogin(data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // async sendLogin() {
    //   let data = null;
    //   try {
    //     data = await this.sendToServer({
    //       url: "users/login/",
    //       args: {
    //         username: this.username,
    //         password: this.password,
    //       },
    //       type: "post",
    //       isAuth: false,
    //     });
    //     this.isLogin = true;
    //     this.saveLogin(data);
    //   } catch (error) {
    //     console.log(error);
    //   }
    // },
    async sendRefreshToken() {
      try {
        let data = await this.sendToServer({
          url: "users/api/token/refresh/",
          args: {
            refresh: this.refreshToken,
          },
          type: "post",
          isAuth: false,
        });
        this.accessToken = data.access;
        localStorage.accessToken = data.access;
        this.isLogin = true;
      } catch (error) {
        console.log(error);
        this.isLogin = false;
      }
    },

    async testServer() {
      try {
        await this.sendToServer({
          url: "users/test/",
          args: { test: "kkk" },
          type: "post",
          isAuth: true,
        });
        this.isLogin = true;
      } catch (error) {
        console.log(error);
        this.sendRefreshToken();
      }
    },
  },
  mounted() {
    this.login();

    const _this = this;
    setInterval(() => {
      _this.sendRefreshToken();
    }, _this.timeTokenAccess);
  },
};
