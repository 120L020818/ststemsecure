<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <el-col :span="24">
          <div class="beg-top-title" style="color:black">系统安全实验</div>
        </el-col>
      </el-header>
      <el-main>
        <el-button type="primary" @click="getperiod">提交</el-button>

        <el-row gutter="20">
          <el-col :span="10">
            <el-card :body-style="{'background':'rgba(176,176,176,0.5)'}">
              <el-form>
                <el-form-item>
                  <el-col :span="12">
                    <el-input v-model="gameName" placeholder="请在此处写入需要监视的游戏名称："/>
                    <el-form-item>
                      <!--                      <el-button type="primary" @click="onSubmit">提交</el-button>-->
                      <el-button type="primary" @click="onSubmit">提交</el-button>
                    </el-form-item>
                  </el-col>
                  <el-col :span="12">
                    <el-input v-model="gameName2" placeholder="请在此处写入需要移除监视的游戏名称："/>
                    <el-form-item>
                      <el-button type="primary" @click="onSubmit2">提交</el-button>
                    </el-form-item>
                  </el-col>
                </el-form-item>

              </el-form>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card :body-style="{'background':'rgba(176,176,176,0.5)'}">
              <el-form>
                <el-form-item>
                  <el-button disabled plain type="primary">
                    请点击下方按钮下载监视软件与配置文件：
                  </el-button>
                </el-form-item>
                <el-form-item>
                  <el-button plain type="primary" @click="onDownload">
                    下载程序
                  </el-button>
                  <el-button plain type="primary" @click="onDownload2">
                    下载配置文件
                  </el-button>
                </el-form-item>
              </el-form>


            </el-card>
          </el-col>
        </el-row>
        <el-row>

        </el-row>
        <el-table :data="tableData" :row-class-name="tableRowClassName" style="width: 100%"
                  :cell-style="{'background':'rgba(176,176,233,0.5)'}">
          <el-table-column prop="game" label="游戏名称" width="180"/>
          <el-table-column prop="avatime" label="最大时长" width="180"/>
          <el-table-column prop="lasttime" label="上次运行时间" width="180"/>
          <el-table-column prop="runningtime" label="已运行时间" width="180"/>
          <el-table-column prop="wrongtime" label="不当游戏次数" width="180"/>
          <el-table-column prop="period1" label="0-6点游戏次数" width="180"/>
          <el-table-column prop="period2" label="6-12点游戏次数" width="180"/>
          <el-table-column prop="period3" label="12-18点游戏次数" width="180"/>
          <el-table-column prop="period4" label="18-24点游戏次数" width="180"/>
          <el-table-column label="操作" style="text-align: right;">
            <template #default="scope">
              <el-button @click="kill(scope.$index)"></el-button>
              <!--              <el-button link type="primary" size="big" @click="handleClickPass(scope.$index)">通过</el-button>-->
              <!--              <el-button link type="primary" size="big" @click="handleClickRefuse(scope.$index)">拒绝</el-button>-->
            </template>
          </el-table-column>

        </el-table>
      </el-main>
    </el-container>
  </div>


</template>

<script>
import axios from "axios"
import APIS from "@/modules/api"
import {
  ElCard,
  ElButton,
  ElRow,
  ElCol,
  ElMain,
  ElContainer,
  ElHeader,
  ElTable,
  ElTableColumn,
  ElForm,
  ElFormItem,
  ElInput,
} from "element-plus";

export default {
  name: "MyTest",
  components: {
    ElCard,
    ElButton,
    ElRow,
    ElCol,
    ElMain,
    ElContainer,
    ElHeader,
    ElTable,
    ElTableColumn,
    ElForm,
    ElFormItem,
    ElInput,
  },
  data: () => ({
    tableData: "",
    gameName: "",
    gameName2: "",
    username: "",
    count: 0
  }),
  mounted() {
    this.query();
    this.timer = setInterval(this.query, 5000);
    this.timer = setInterval(this.update, 5000);
  },
  methods: {
    getperiod() {
      var mydata = {
        "temp": 2333
      }
      axios.post(APIS.getperiod, mydata
      ).then(res => {
        console.log(res.data.success)
      })
    },
    kill(index) {
      console.log(this.tableData[index]);
      var mydata = {
        "gamename": this.tableData[index].game
      }
      axios.post(APIS.kill, mydata
      ).then(res => {
        console.log(res.data.success)
      })
    },
    warning() {
      axios.post(APIS.email, {
            'username': this.username
          }
      ).then(res => {
        console.log(res.data.success)
      })
    },
    getusername() {
      axios.post(APIS.getusername, {
            'data': 233
          }
      ).then(res => {
        console.log(res.data)
        this.username = res.data.username
        console.log(this.username)
        this.warning()
      })
    },
    tableRowClassName({row, rowIndex}) {
      var first = row['avatime'] * 3600;
      var list = row['runningtime'].split(':')
      console.log(row['runningtime'])
      console.log(list)
      var second = 0
      var mylen = list.length
      if (mylen === 3) {
        second = Number(list[0]) * 3600 + Number(list[1]) * 60 + Number(list[2]);
      } else {
        second = Number(list[0]) * 60 + Number(list[1]);
      }

      console.log('first' + first)
      console.log('seconde' + second)
      // console.log(row[0])
      if (this.count === 0 && second > first) {
        this.getusername();
        this.count++;
        return 'warning-row';
      } else if (this.count !== 0 && second > first) {
        return 'warning-row';
      } else {
        return '';
      }
    },
    update() {
      var innerData = "";
      axios.post(APIS.second, {}
      ).then(res => {
        innerData = res.data.mydata
        this.tableData = innerData
        console.log(res.data.success)
      })
    },
    query() {
      var innerData = "";
      axios.post(APIS.second, {}
      ).then(res => {
        innerData = res.data.mydata
        this.tableData = innerData
        console.log(res.data.success)
      })
    },

    onDownload() {
      axios.post(APIS.download1, {data: "hahahaha"}
      ).then(res => {
        const a = document.createElement('a')
        a.style.display = 'none'
        a.href = window.URL.createObjectURL(new Blob([res.data]))
        a.setAttribute('download', 'vision.exe') //设置文件名
        document.body.appendChild(a)
        a.click()
        document.body.removeChild(a)
      })
    },onDownload2() {
      axios.post(APIS.download2, {data: "hahahaha"}
      ).then(res => {
        const b = document.createElement('a')
        b.style.display = 'none'
        b.href = window.URL.createObjectURL(new Blob([res.data]))
        b.setAttribute('download', 'user.json') //设置文件名
        document.body.appendChild(b)
        b.click()
        document.body.removeChild(b)
      })
    },
    onSubmit2() {
      if (this.gameName2 === "") {
        return;
      }
      var innerData = "";
      axios.post(APIS.dele, {game: this.gameName2}
      ).then(res => {
        innerData = res.data.mydata
        this.tableData = innerData
        console.log(res.data.success)
      })
    },
    onSubmit() {
      if (this.gameName === "") {
        return;
      }
      var innerData = "";
      axios.post(APIS.test, {game: this.gameName}
      ).then(res => {
        innerData = res.data.mydata
        this.tableData = innerData
        console.log(res.data.success)
      })
    }
  }
}

</script>

<style>
@import "../styles/common.css";

.el-table .warning-row {
  background: rgba(255, 0, 0, 0.2);
}

.common-layout {
  width: 100%;
  height: 100vh;
  position: fixed;
  /*overflow-x: hidden;*/
  /*overflow-y: hidden;*/
  background-size: cover !important;
  background-image: url(../assets/bg.png);
}

.el-row {
  margin-bottom: 20px;
}

.el-row:last-child {
  margin-bottom: 0;
}

.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
}

.beg-top-title {
  /*line-height: 200px;*/
  text-align: center;
  /*height: 200px;*/
  /*weight: 500px;*/
  /*margin-top: 100px;*/
  /*font-size: 72px;*/
  font-family: "Aa新华墨竹体 (非商业使用)", serif;
  background-color: rgba(255, 255, 255, 0.7);
}
</style>