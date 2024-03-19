function person(name,age,Lname){
    this.name = name
    this.age = age
    this.Lname = Lname
    this.id = function() {
        document.write(this.name + this.Lname + this.age)
      };
}

const person1 = new person("Luka", 22, "Razikashvili")
person1.id();