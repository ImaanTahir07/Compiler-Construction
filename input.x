~~declare number age = 22;
declare text name = "Emaan";

output("Name: " + name);
output("Age: " + age);~~



~~declare boolean isStudent = yes;

condition (isStudent) {
    output("The person is a student.");
} otherwise {
    output("The person is not a student.");
}~~



~~declare list array = [1, 2, 3, 4, 5];

loop (number i = 0; i < array.length; i++) {
    output("Number: " + array[i]);
    condition (array[i] == 3) {
        output("Found number 3, exiting loop.");
        exit;
    }
}~~



~~declare integer add(integer a, integer b) {
    give_back a + b;
}

declare integer result = add(5, 10);
output("Sum: " + result);~~







~~ blueprint Animal {
    empty makeSound() {
        output("Animal sound");
    }
}

blueprint Dog inherits Animal {
    empty makeSound() {
        output("Bark");
    }
}

declare Dog myDog = Dog();
myDog.makeSound();  ~~




~~attempt {
    output("Attempting risky operation.");
} handle (exception e) {
    output("Handled an exception: " + e.message);
} conclude {
    output("Tidying up resources.");
}~~



~~base blueprint Shape {
    declare text color;

    initializer(string color) {
        self.color = color;
    }
    empty displayColor() {
        output("Color: " + self.color);
    }
}

blueprint Circle inherits Shape {
    declare number radius;

    initializer(text color, number radius) {
        Shape(color);  
        self.radius = radius;
    }

    empty displayRadius() {
        output("Radius: " + self.radius);
    }
}

declare Circle myCircle = Circle("Red", 10); 
myCircle.displayColor();  
myCircle.displayRadius();  ~~





~~declare boolean isEven(number a) {
    condition (a % 2 == 0) {
        give_back yes;
    } otherwise {
        give_back no;
    }
}

declare number a = 4;
condition (isEven(a)) {
    output(a + " is even.");
} otherwise {
    output(a + " is odd.");
}~~


blueprint Person {
    declare text name;
    declare number age;

    constructor(text name, number age) {
        self.name = name;
        self.age = age;
    }

    empty introduce() {
        output("Hello, my name is " + self.name + " and I am " + self.age + " years old.");
    }
}

declare Person emaan = Person("Emaan", 22);
emaan.introduce();  














