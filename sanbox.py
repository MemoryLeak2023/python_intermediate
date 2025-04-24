def greeting_replicator(greeting, reps):
  replicated = greeting * reps
  def print_replicated_greeting():
    print(replicated)
  print_replicated_greeting()

greeting_replicator("hello ", 3)