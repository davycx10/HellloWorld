use std::{env, process::Command};
mod hello_from;
mod hello_to;

fn main(){
    let args: Vec<String> = env::args().collect();

    if args.len() < 3{
        eprint!("Use: carga run --from | to <name>");
        return;
    }

    let command = &args[1];
    let name = &args[2];

    let message = match command.as_str() {
        "from" => from::helloFrom(name),
        "to" => to::helloTo(name),

    };
}