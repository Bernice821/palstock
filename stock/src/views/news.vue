<template>
  <div style="margin-left:3%;">
    <h3 class="text-2xl font-bold py-2" style="color:#1B3C73;text-align:left;font-size: 30px">股票新聞</h3>
    <h4 class="text-xl font-bold py-2" style="color:#1B3C73;text-align:left">最新新聞</h4>
    <div>
      <b-container>
        <b-row cols="1" cols-md="2" cols-xl="3">
          <b-col v-for="news in getRecentNews">
            <a v-bind:href="news.Url">
              <div class="news img-on-top">
                <img class="news-img" v-bind:src="news.ImgUrl">
                <div class="news-content">
                  <h5 class="news-title" v-bind:title="news.Title">{{news.Title}}</h5>
                  <span class="news-date">{{news.Time}}</span>
                </div>
              </div>
            </a>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  name: 'App',
  compatConfig: { MODE: 3 },
  data() {
    return {
      recentNews: [
        {
          "Title": "Rick Astley - Never Gonna Give You Up",
          "Url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
          "ImgUrl": "https://i.ytimg.com/vi/dQw4w9WgXcQ/hq720.jpg",
          "Time": "2009 年 10 月 25 日"
        }
      ]
    };
  },
  computed: {
    getRecentNews() {
      return this.recentNews;
    }
  },
  methods: {
    async fetchNews() {
      try {
        const response = await axios.post('http://127.0.0.1:12000/api/newsStocks', {
          newsNum: 12,
        });
        // const data = response.data;
        this.recentNews = response.data;
      } catch (error) {
        console.error('Error fetching index:', error);
      }
    },
  },
  mounted() {
    this.fetchNews();
  }
}
</script>
<style scoped lang="scss">
.col {
  padding: 0;
}

a {
  color: black;
  text-decoration: none;
}

.news {
  --img-width: 8rem;
  --img-height: 6rem;
  --news-height: 6rem;
  position: relative;
  margin-bottom: 0.5rem;
  /*border: 1px solid #888888;*/
  border-radius: 3px;
  height: var(--news-height);
  transition-duration: 0.5s;
  * {
  text-align: left;
  }
  &:hover {
    /*z-index: 2,*/
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  }
  margin: 2%;
}

.news-img {
  position: absolute;
  z-index: -1;
  left: 0;
  width: var(--img-width);
  height: var(--img-height);
  border-radius: 3px;
  object-fit: cover;
}

.news-content {
  margin-left: var(--img-width);
  padding: 0.25rem;
}

.news.img-on-top {
  --img-width: 100%;
  --img-height: 15rem;
  --news-height: calc(var(--img-height) + 6rem);
  .news-img {
    position: relative;
  }
  .news-content {
    margin-left: 0;
  }
}

.news-title {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;  
  font-size: 1.125rem;
  /*height: 2em;*/
  margin-bottom: 0;
  overflow: hidden;
}

.news-source, .news-date, .news-article {
  font-size: 0.75rem;
  color: #888888;
}

.news-source:after {
  content: "．"
}

.news-article {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;  
  overflow: hidden;
  display: none;
}

.card4 {
  margin-top: 2%;
  margin-left: 2%;
  border-radius: 2px;
  padding: 20px;
  overflow: hidden;
  box-shadow: 0 4px 8px 0 rgba(182, 182, 182, 0.8);
  transition: 0.3s;
  width: 30%;
  height: 90%;
}

h1 {
  font-size: 22px;
  color: #333;
  font-weight: 600;
  text-align: center;
  margin-bottom: 1.4rem;
}

.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  flex-wrap: wrap;
  gap: 10px;
}

.media {
  width: 180px;
  height: 130px;
  overflow: hidden;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 4px 8px 0 rgba(182, 182, 182, 0.8);
  transition: 0.3s;
}

.media img {
  width: 100%;
  height: 100%;
}

.layer {
  opacity: 0;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 10px;
  height: 90%;
  background: #fff;
  color: #151e3f;
  transition: all 0.9s ease;

  p {
    transition: all 0.9s ease;
    transform: scale(0.1);
  }
}

p {
  text-align: center;
  font-size: 15px;
  letter-spacing: 1px;
}

.media:hover .layer {
  opacity: 0.8;
  width: 90%;
  transition: all 0.5s ease;

  p {
    transform: scale(1);
    transition: all 0.9s ease;
  }
}
</style>
