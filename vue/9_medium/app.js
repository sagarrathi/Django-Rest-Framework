function get_random_value(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

const app = Vue.createApp({
  data() {
    return {
      hero_health: 100,
      monster_health: 100,
      round_counter: 0,
      game_end: false,
      winner: "No One",
      log_messages:[],
    };
  },

  methods: {
    attack_monster() {
      this.round_counter += 1;
      const attack_value = get_random_value(5, 12);
      this.monster_health -= attack_value;
      this.add_log_message("hero", "attack", attack_value);
      this.attack_hero();
    },

    attack_hero() {
      // const attack_value=10;
      const attack_value = get_random_value(8, 12);
      this.hero_health -= attack_value;
      this.add_log_message("monster", "attack", attack_value);
    },

    attack_monster_special() {
      this.round_counter += 1;
      const attack_value = get_random_value(10, 25);
      this.monster_health -= attack_value;
      this.attack_hero();
      this.add_log_message("hero", "special attack", attack_value);
    },

    heal_hero() {
      this.round_counter += 1;
      const heal_value = get_random_value(8, 12);
      
      this.hero_health += heal_value;
      this.attack_hero();
      this.add_log_message("hero", "heals", heal_value);
    },

    surrender(){
      this.winner="Monster";
      this.game_end=true;
      this.add_log_message("hero", "surrender", "to monster")
    },


    log_winner() {
      console.log(this.winner);
    },

    
    start_game(){
      this.hero_health= 100;
      this.monster_health= 100;
      this.round_counter= 0;
      this.game_end= false;
      this.winner= "No One";
      this.log_messages=[];
    },
  
    add_log_message(who, what, value){
      this.log_messages.unshift({
        action_by :who,
        action_type: what,
        action_value: value
      });

    },

  },

  watch: {
    hero_health(value) {
      // console.log("runninng hero watcher")
      if (value > 100) {
        this.hero_health = 100;
      }
      if (value <= 0 && this.monster_health > 0) {
        this.winner = "Monster";
        this.game_end = true;
      } else if (value <= 0 && this.monster_health <= 0) {
        this.game_end = true;
      }
    },
    monster_health(value) {
      // console.log("runninng monster watcher")
      if (value > 100) {
        this.hero_health = 100;
      }
      if (value <= 0 && this.hero_health > 0) {
        this.winner = "Hero";
        this.game_end = true;
      } else if (value <= 0 && this.hero_health <= 0) {
        this.game_end = true;
      }
    },

    
    game_end(value) {
      console.log("runninng game_end watcher");
      this.log_winner();
    },
  },

  computed: {
    monster_bar_style() {
      if (this.monster_health < 0) {
        return {width: '0%'};
      }
      else {
        return { width: this.monster_health + "%" };
      }
     
    },

  hero_bar_style() {
    if (this.hero_health < 0) {
      return {width: '0%'};
    }
    else {
      return { width: this.hero_health + "%" };
    }
    },

    may_use_special_attack() {
      return this.round_counter % 3 !== 0;
    },
  },
});

app.mount("#game");
