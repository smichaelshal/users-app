import axios from "axios";

export default {
  name: "SendApi",
  data() {
    return {
      accessToken: null,
      host: "http://localhost:8000/",
    };
  },
  methods: {
    sendToServer(kwargs) {
      const url = this.host + kwargs["url"];
      const args = kwargs["args"] ? kwargs["args"] : {};
      const type = kwargs["type"] ? kwargs["type"] : "post";
      let isAuth;

      if (kwargs["isAuth"] === undefined) {
        isAuth = true;
      } else {
        isAuth = kwargs["isAuth"];
      }
      let config = {};

      if (isAuth) {
        config = {
          Authorization: `Bearer ${this.accessToken}`,
        };
      }

      return axios({
        method: type,
        url: url,
        data: args,
        headers: config,
      })
        .then((response) => {
          return response.data;
        })
        .catch((error) => {
          throw error.response;
        });
    },
  },
};
