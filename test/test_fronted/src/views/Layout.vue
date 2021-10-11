<template>
<v-app>
    <!-- 侧边栏 -->
  <v-navigation-drawer app>
    <template>

      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Application
          </v-list-item-title>
          <v-list-item-subtitle>
            subtext
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :href="item.link"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </template>
  </v-navigation-drawer>

<!-- 顶部栏 -->
  <v-app-bar app>
    霍格沃兹测试平台
  </v-app-bar>

<!-- 内容正文 -->
  <v-main>

    <!-- 给应用提供合适的间距 -->
        
      <!-- 如果使用 vue-router -->
      <!-- 在v-main中放置子路由 -->
      <router-view></router-view>
  </v-main>

  <v-footer app>
    <!-- -->
  </v-footer>
</v-app>
</template>

<script>
// 存放js脚本

  export default {
    //   存放数据
    data () {
      return {
        items: [
          { title: '测试用例', icon: 'mdi-view-dashboard', link: "testcase"},
          { title: '测试任务', icon: 'mdi-image',link:"task" },
          { title: '测试报告', icon: 'mdi-help-box' },
        ],
        right: null,
      }
    },
  }
</script>