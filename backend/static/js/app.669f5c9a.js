(function(){"use strict";var e={2139:function(e,t,o){var a=o(5130),s=o(6768);function r(e,t,o,a,r,n){const l=(0,s.g2)("BaseComponent");return(0,s.uX)(),(0,s.Wv)(l)}o(8992),o(4520);var n=o(4232);const l={key:0},i={key:1},u={class:"col-12"},c={class:"card col-10 col-lg-3 col-md-6 col-sm-6"},d={class:"card-header"},m={key:0},k={class:"card-body"},h={class:"card-footer"},g={class:"footer-content"},p={class:"itens-count"},f={href:"#"},v={class:"delete-itens"};function b(e,t,o,a,r,b){const y=(0,s.g2)("LoginComponent"),S=(0,s.g2)("v-btn"),C=(0,s.g2)("InputGroup1"),L=(0,s.g2)("TodoItems");return(0,s.uX)(),(0,s.CE)(s.FK,null,[b.isUserLoggedIn?(0,s.Q3)("",!0):((0,s.uX)(),(0,s.CE)("div",l,[(0,s.bF)(y,{onSendData:b.handleLogin},null,8,["onSendData"])])),b.isUserLoggedIn?((0,s.uX)(),(0,s.CE)("div",i,[(0,s.bF)(S,{color:"primary mb-4",onClick:b.logout},{default:(0,s.k6)((()=>t[1]||(t[1]=[(0,s.eW)(" Logout ")]))),_:1},8,["onClick"])])):(0,s.Q3)("",!0),(0,s.Lk)("div",u,[(0,s.Lk)("div",c,[(0,s.Lk)("div",d,[t[2]||(t[2]=(0,s.Lk)("h3",null,[(0,s.Lk)("strong",null,"TO-DO LIST")],-1)),b.isUserLoggedIn?((0,s.uX)(),(0,s.CE)("p",m,"Usuário logado: "+(0,n.v_)(r.userName),1)):(0,s.Q3)("",!0)]),(0,s.bF)(C,{onCreateTask:b.createTask},null,8,["onCreateTask"]),(0,s.Lk)("div",k,[(0,s.Lk)("ul",null,[(0,s.bF)(L,{items:r.tasks,onDeleteTask:b.deleteTask,onUpdateTask:b.updateTask},null,8,["items","onDeleteTask","onUpdateTask"])])]),(0,s.Lk)("div",h,[(0,s.Lk)("div",g,[(0,s.Lk)("div",p,[(0,s.Lk)("a",f," Tasks: "+(0,n.v_)(r.tasks.filter((e=>0==e.done)).length),1)]),(0,s.Lk)("div",v,[(0,s.Lk)("a",{href:"#",onClick:t[0]||(t[0]=(...e)=>b.deleteAll&&b.deleteAll(...e))},t[3]||(t[3]=[(0,s.Lk)("i",{class:"bi bi-trash3-fill"},null,-1)]))])])])])])],64)}o(4114);var y=o(4373);const S=y.A.create({baseURL:"http://127.0.0.1:5000",timeout:1e4,headers:{"Content-Type":"application/json"}}),C=e=>S.post("/auth",e),L=e=>S.get(`/users/${e}`),w=e=>S.post("/users",e),I=e=>S.post("/tasks",e,{headers:{Authorization:`Bearer ${JSON.parse(localStorage.getItem("token"))}`}}),T=()=>S.get("/tasks",{headers:{Authorization:`Bearer ${JSON.parse(localStorage.getItem("token"))}`}}),_=(e,t)=>S.put(`/tasks/${e}`,t,{headers:{Authorization:`Bearer ${JSON.parse(localStorage.getItem("token"))}`}}),N=e=>S.delete(`/tasks/${e}`,{headers:{Authorization:`Bearer ${JSON.parse(localStorage.getItem("token"))}`}}),V=()=>S.get("/tasks/reset",{headers:{Authorization:`Bearer ${JSON.parse(localStorage.getItem("token"))}`}});const O={class:"input-group mb-3"};function U(e,t,o,r,n,l){return(0,s.uX)(),(0,s.CE)("div",O,[(0,s.bo)((0,s.Lk)("input",{onKeypress:t[0]||(t[0]=(...e)=>l.onKeyPress&&l.onKeyPress(...e)),"onUpdate:modelValue":t[1]||(t[1]=e=>n.value=e),type:"text",class:"form-control p-2",placeholder:"Task item","aria-label":"Task item","aria-describedby":"button-addon2"},null,544),[[a.Jo,n.value,void 0,{trim:!0}]]),(0,s.Lk)("button",{onClick:t[2]||(t[2]=(...e)=>l.emitValue&&l.emitValue(...e)),class:"btn btn-primary",type:"button",id:"button-addon2"},"Button")])}var A={emits:["create-task"],props:{},data(){return{value:""}},methods:{emitValue(){""!=this.value&&this.$emit("create-task",this.value),this.value=""},onKeyPress(e){"Enter"==e.key&&this.emitValue()}}},F=o(1241);const x=(0,F.A)(A,[["render",U]]);var E=x;const $={class:"item-box"},P={class:"form-check"},X=["value","id","onUpdate:modelValue"],J=["for"],j=["onClick"];function B(e,t,o,r,l,i){return(0,s.uX)(!0),(0,s.CE)(s.FK,null,(0,s.pI)(o.items,((e,o)=>((0,s.uX)(),(0,s.CE)("li",{key:o},[(0,s.Lk)("div",$,[(0,s.Lk)("div",P,[(0,s.bo)((0,s.Lk)("input",{class:"form-check-input",type:"checkbox",value:e._id,id:"flexCheckChecked-"+o,"onUpdate:modelValue":t=>e.done=t,onChange:t[0]||(t[0]=(...e)=>i.handleCheck&&i.handleCheck(...e))},null,40,X),[[a.lH,e.done]]),(0,s.Lk)("label",{class:"form-check-label",for:"flexCheckChecked-"+o},[(0,s.Lk)("a",{class:(0,n.C4)({active:e.done}),href:"#"},(0,n.v_)(e.task),3)],8,J)]),(0,s.Lk)("a",{href:"#",onClick:t=>i.emitKey(e._id)},t[1]||(t[1]=[(0,s.Lk)("i",{class:"bi bi-x-lg"},null,-1)]),8,j)])])))),128)}var D={emits:["delete-task","update-task"],props:{items:{type:Array,require:!0}},methods:{emitKey(e){this.$emit("delete-task",e)},handleCheck(e){const t={id:e.target.value,update:{done:e.target.checked}};this.$emit("update-task",t)}}};const K=(0,F.A)(D,[["render",B]]);var M=K;const W={key:0},Q={key:1};function z(e,t,o,r,n,l){const i=(0,s.g2)("v-btn"),u=(0,s.g2)("v-text-field"),c=(0,s.g2)("v-form"),d=(0,s.g2)("v-sheet"),m=(0,s.g2)("v-overlay");return(0,s.uX)(),(0,s.CE)(s.FK,null,[(0,s.bF)(i,{color:"primary mb-4",onClick:t[0]||(t[0]=t=>e.overlay=!e.overlay)},{default:(0,s.k6)((()=>t[13]||(t[13]=[(0,s.eW)(" Login ")]))),_:1}),(0,s.bF)(m,{class:"align-center justify-center",modelValue:e.overlay,"onUpdate:modelValue":t[12]||(t[12]=t=>e.overlay=t),contained:""},{default:(0,s.k6)((()=>[e.haveAccount?((0,s.uX)(),(0,s.Wv)(d,{key:0,class:"mx-auto",width:"300"},{default:(0,s.k6)((()=>[(0,s.bF)(c,{onSubmit:t[3]||(t[3]=(0,a.D$)((()=>{}),["prevent"]))},{default:(0,s.k6)((()=>[(0,s.bF)(u,{modelValue:e.username,"onUpdate:modelValue":t[1]||(t[1]=t=>e.username=t),modelModifiers:{trim:!0},rules:e.rulesName,label:"User Login"},null,8,["modelValue","rules"]),(0,s.bF)(u,{modelValue:e.password,"onUpdate:modelValue":t[2]||(t[2]=t=>e.password=t),modelModifiers:{trim:!0},rules:e.rulesPass,label:"Password",type:"password"},null,8,["modelValue","rules"]),(0,s.bF)(i,{class:"mt-2",type:"submit",onClick:l.emitLogin,block:""},{default:(0,s.k6)((()=>t[14]||(t[14]=[(0,s.eW)("Login")]))),_:1},8,["onClick"])])),_:1}),(0,s.bF)(i,{class:"mt-2",type:"submit",variant:"plain",onClick:t[4]||(t[4]=t=>e.haveAccount=!1),block:""},{default:(0,s.k6)((()=>t[15]||(t[15]=[(0,s.eW)("create account")]))),_:1})])),_:1})):(0,s.Q3)("",!0),e.haveAccount?(0,s.Q3)("",!0):((0,s.uX)(),(0,s.Wv)(d,{key:1,class:"mx-auto",width:"300"},{default:(0,s.k6)((()=>[(0,s.bF)(c,{onSubmit:t[11]||(t[11]=(0,a.D$)((()=>{}),["prevent"]))},{default:(0,s.k6)((()=>[(0,s.bF)(u,{modelValue:e.name,"onUpdate:modelValue":t[5]||(t[5]=t=>e.name=t),modelModifiers:{trim:!0},rules:e.rules,label:"User Name"},null,8,["modelValue","rules"]),(0,s.bF)(u,{modelValue:e.username,"onUpdate:modelValue":t[6]||(t[6]=t=>e.username=t),modelModifiers:{trim:!0},rules:e.rulesName,label:"User Login",onFocus:t[7]||(t[7]=t=>e.exist=!1)},null,8,["modelValue","rules"]),(0,s.bF)(u,{modelValue:e.password,"onUpdate:modelValue":t[8]||(t[8]=t=>e.password=t),modelModifiers:{trim:!0},rules:e.rulesPass,label:"Password",type:"password"},null,8,["modelValue","rules"]),(0,s.bF)(u,{modelValue:e.r_password,"onUpdate:modelValue":t[9]||(t[9]=t=>e.r_password=t),modelModifiers:{trim:!0},label:"Repeat Password",type:"password",onFocus:t[10]||(t[10]=t=>e.pwdAlert=!1)},null,8,["modelValue"]),e.pwdAlert?((0,s.uX)(),(0,s.CE)("span",W,t[16]||(t[16]=[(0,s.Lk)("strong",{class:"text-red-lighten-1"},"password not match",-1)]))):(0,s.Q3)("",!0),e.exist?((0,s.uX)(),(0,s.CE)("span",Q,t[17]||(t[17]=[(0,s.Lk)("strong",{class:"text-red-lighten-1"},"user already registered",-1)]))):(0,s.Q3)("",!0),(0,s.bF)(i,{class:"mt-2",type:"submit",onClick:l.emitData,block:""},{default:(0,s.k6)((()=>t[18]||(t[18]=[(0,s.eW)("Create account")]))),_:1},8,["onClick"])])),_:1})])),_:1}))])),_:1},8,["modelValue"])],64)}var Y={emits:["send-data"],data:()=>({exist:!1,pwdAlert:!1,haveAccount:!0,overlay:!1,name:"",rules:[e=>!!e||"You must enter your user Name"],username:"",rulesName:[e=>!!e||"You must enter your user login"],r_password:"",password:"",rulesPass:[e=>!!e||"You mus enter you password"]}),methods:{emitLogin(){if(""!==this.username&&""!==this.password){const e={username:this.username,password:this.password};this.$emit("send-data",e)}},emitData(){if(""!==this.username&&""!==this.password)if(this.password!==this.r_password)this.pwdAlert=!0;else{const e={name:this.name,user_login:this.username,pwd:this.password};L(e.user_login).then((e=>{console.log(e.data),e.data&&(this.exist=!0)})).catch((t=>{t.response&&404===t.response.status?(console.log("Usuário não encontrado. Prosseguindo com o cadastro..."),console.log(e),w(e).then((e=>{console.log(e),alert("Usuário criado!"),location.reload()}))):console.error("Erro ao verificar usuário:",t)}))}}}};const G=(0,F.A)(Y,[["render",z]]);var R=G,q={name:"BaseComponent",components:{InputGroup1:E,TodoItems:M,LoginComponent:R},data(){return{tasks:[],itens:0,userName:localStorage.getItem("userName")||""}},computed:{isUserLoggedIn(){return!!this.userName}},mounted(){if(this.verifyToken())T().then((e=>{this.tasks=e.data["data"],console.log(this.tasks)})).catch((e=>{console.log("Error fetching tasks",e),localStorage.removeItem("token"),localStorage.removeItem("userName"),location.reload()}));else{const e=localStorage.getItem("task");localStorage.removeItem("userName"),e&&(this.tasks=JSON.parse(e),this.itens=this.tasks.length)}},methods:{createTask(e){if(this.verifyToken()){const t={task:e,done:!1};I(t).then((e=>{console.log("msg",e.data),this.getTask()})).catch((e=>{console.log("error",e),localStorage.removeItem("token"),localStorage.removeItem("userName"),location.reload()}))}else{this.itens++;const t={_id:this.itens,task:e,done:!1};this.tasks.push(t),localStorage.setItem("task",JSON.stringify(this.tasks))}},getTask(){T().then((e=>{this.tasks=e.data["data"]})).catch((e=>{console.log("Error fetching tasks",e),localStorage.removeItem("token"),localStorage.removeItem("userName"),location.reload()}))},updateTask(e){this.verifyToken()?_(e.id,e.update).then((e=>{console.log("msg",e.data),this.getTask()})).catch((e=>{console.log("Erro ao atualizar task",e),this.getTask()})):localStorage.setItem("task",JSON.stringify(this.tasks))},deleteTask(e){if(this.verifyToken())N(e).then((e=>{console.log("msg",e.data),this.getTask()})).catch((e=>{console.log("error",e),localStorage.removeItem("token"),localStorage.removeItem("userName"),location.reload()}));else{const t=this.tasks.findIndex((t=>t._id==e));console.log(t),this.tasks.splice(t,1),localStorage.setItem("task",JSON.stringify(this.tasks))}},deleteAll(){this.verifyToken()?V().then((e=>{console.log("msg",e.data),this.getTask()})).catch((e=>{console.log("error",e),localStorage.removeItem("token"),localStorage.removeItem("userName"),location.reload()})):this.tasks=[]},getUser(e){L(e).then((e=>{const{data:t}=e;localStorage.setItem("userName",t.user.name),location.reload()})).catch((e=>e))},verifyToken(){return localStorage.getItem("token")},handleLogin(e){C(e).then((t=>{const o=JSON.stringify(t.data.token);localStorage.setItem("token",o),this.getUser(e.username)})).catch((e=>{alert(e.code)}))},logout(){localStorage.removeItem("token"),localStorage.removeItem("userName"),location.reload()}}};const H=(0,F.A)(q,[["render",b]]);var Z=H,ee={name:"App",components:{BaseComponent:Z}};const te=(0,F.A)(ee,[["render",r]]);var oe=te,ae=(o(5524),o(7768)),se=o(1920),re=o(5741);const ne=(0,ae.$N)({components:se,directives:re});(0,a.Ef)(oe).use(ne).mount("#app")}},t={};function o(a){var s=t[a];if(void 0!==s)return s.exports;var r=t[a]={exports:{}};return e[a].call(r.exports,r,r.exports,o),r.exports}o.m=e,function(){var e=[];o.O=function(t,a,s,r){if(!a){var n=1/0;for(c=0;c<e.length;c++){a=e[c][0],s=e[c][1],r=e[c][2];for(var l=!0,i=0;i<a.length;i++)(!1&r||n>=r)&&Object.keys(o.O).every((function(e){return o.O[e](a[i])}))?a.splice(i--,1):(l=!1,r<n&&(n=r));if(l){e.splice(c--,1);var u=s();void 0!==u&&(t=u)}}return t}r=r||0;for(var c=e.length;c>0&&e[c-1][2]>r;c--)e[c]=e[c-1];e[c]=[a,s,r]}}(),function(){o.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return o.d(t,{a:t}),t}}(),function(){o.d=function(e,t){for(var a in t)o.o(t,a)&&!o.o(e,a)&&Object.defineProperty(e,a,{enumerable:!0,get:t[a]})}}(),function(){o.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){o.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){var e={524:0};o.O.j=function(t){return 0===e[t]};var t=function(t,a){var s,r,n=a[0],l=a[1],i=a[2],u=0;if(n.some((function(t){return 0!==e[t]}))){for(s in l)o.o(l,s)&&(o.m[s]=l[s]);if(i)var c=i(o)}for(t&&t(a);u<n.length;u++)r=n[u],o.o(e,r)&&e[r]&&e[r][0](),e[r]=0;return o.O(c)},a=self["webpackChunkvue_todo_2"]=self["webpackChunkvue_todo_2"]||[];a.forEach(t.bind(null,0)),a.push=t.bind(null,a.push.bind(a))}();var a=o.O(void 0,[504],(function(){return o(2139)}));a=o.O(a)})();
//# sourceMappingURL=app.669f5c9a.js.map