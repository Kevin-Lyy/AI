#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// X is player 1
// O is player 2

// [b0,b1,b2]
// [b3,b4,b5]
// [b6,b7,b8]

int rand(void);

int checkplayer(int i, char * board){
  if(board[i] == 'X'){
    return 1;
  }
  else if(board[i] == 'O'){
    return 2;
  }
}

int checkboard(int x, int y, int z, char * board){
  if(board[x] == board[y] && board[x] == board[z]){
    return 1;
  }
  return 0;
}

int checkwinner(char * board){

  //row 1- works
  if(checkboard(0,1,2,board)){
    return checkplayer(0,board);
  }

  //row 2- works
  else if(checkboard(3,4,5,board)){
    return checkplayer(3,board);
  }

  //column 1- works
  else if(checkboard(0,3,6,board)){
    return checkplayer(0,board);
  }

  //column 2- works
  else if(checkboard(1,4,7,board)){
    return checkplayer(1,board);
  }

  //column 3- works
  else if(checkboard(2,5,8,board)){
    return checkplayer(2,board);
  }

  //diagonal left- works
  else if(checkboard(0,4,8,board)){
    return checkplayer(0,board);
  }

  //diagonal right- works
  else if(checkboard(2,4,6,board)){
    return checkplayer(6,board);

  }

  //counter to check if the board is still full of  -
  //adds 1 to a counter if the spot is taken by x or o
  else{
    int c = 0;
    int counter = 0;
    for(;c < 9;c++){
      if(board[c] != '-'){
        counter++;
      }
    }

    //if the board is full it returns a 3 which means it is a tie
    if(counter == 9){
      return 3;
    }
  }
  //returns a 0 which means no one wins and it is not a tie
  return 0;
}

int lastwinner(char * board){
  //row 3- works
  if(checkboard(6,7,8,board)){
    return checkplayer(6,board);
  }
}

void printboard(char * board){
  int i = 0;
  for(;i < 3;i++){
    printf("%c ",board[i]);
  }
  printf("\n");
  for(;i < 6;i++){
    printf("%c ",board[i]);
  }
  printf("\n");
  for(;i < 9;i++){
    printf("%c ",board[i]);
  }
  printf("\n");

}

int corner(){
  int num = rand() % 10;
  if(num <= 3){
    return 0;
  }
  if(num < 6){
    return 2;
  }
  if(num <= 8){
    return 6;
  }
  else{
    return 8;
  }
}

void finish_board_ai(char * board){
  if(board[0] == '-' && (board[1] == 'O' && board[2] == 'O' || board[3] == 'O' && board[6] == 'O' || board[4] == 'O' && board[8] == 'O') ){
    board[0] = 'O';
  }
  else if(board[1] == '-' && (board[0] == 'O' && board[2] == 'O' || board[4] == 'O' && board[7] == 'O')){
    board[1] = 'O';
  }
  else if(board[2] == '-' && (board[1] == 'O' && board[0] == 'O' || board[5] == 'O' && board[8] == 'O' || board[4] == 'O' && board[6] == 'O')){
    board[2] = 'O';
  }
  else if(board[3] == '-' && (board[0] == 'O' && board[6] == 'O' || board[4] == 'O' && board[5] == 'O')){
    board[3] = 'O';
  }
  else if(board[4] == '-' && (board[0] == 'O' && board[8] == 'O' || board[1] == 'O' && board[7] == 'O' || board[2] == 'O' && board[6] == 'O') || board[3] == 'O' && board[5] == 'O'){
    board[4] = 'O';
  }
  else if(board[5] == '-' && (board[2] == 'O' && board[8] == 'O' || board[3] == 'O' && board[4] == 'O')){
    board[5] = 'O';
  }
  else if(board[6] == '-' && (board[0] == 'O' && board[3] == 'O' || board[2] == 'O' && board[4] == 'O' || board[7] == 'O' && board[8] == 'O')){
    board[6] = 'O';
  }
  else if(board[7] == '-' && (board[1] == 'O' && board[4] == 'O' || board[6] == 'O' && board[8] == 'O')){
    board[7] = 'O';
  }
  else if(board[8] == '-' && (board[0] == 'O' && board[4] == 'O' || board[2] == 'O' && board[5] == 'O' || board[6] == 'O' && board[7] == 'O')){
    board[8] = 'O';
  }
}

void endplayer(char * board){
  if(board[0] == '-' && (board[1] == 'X' && board[2] == 'X' || board[3] == 'X' && board[6] == 'X' || board[4] == 'X' && board[8] == 'X') ){
    board[0] = 'O';
  }
  else if(board[1] == '-' && (board[0] == 'X' && board[2] == 'X' || board[4] == 'X' && board[7] == 'X')){
    board[1] = 'O';
  }
  else if(board[2] == '-' && (board[1] == 'X' && board[0] == 'X' || board[5] == 'X' && board[8] == 'X' || board[4] == 'X' && board[6] == 'X')){
    board[2] = 'O';
  }
  else if(board[3] == '-' && (board[0] == 'X' && board[6] == 'X' || board[4] == 'X' && board[5] == 'X')){
    board[3] = 'O';
  }
  else if(board[4] == '-' && (board[0] == 'X' && board[8] == 'X' || board[1] == 'X' && board[7] == 'X' || board[2] == 'X' && board[6] == 'X') || board[3] == 'X' && board[5] == 'X'){
    board[4] = 'O';
  }
  else if(board[5] == '-' && (board[2] == 'X' && board[8] == 'X' || board[3] == 'X' && board[4] == 'X')){
    board[5] = 'O';
  }
  else if(board[6] == '-' && (board[0] == 'X' && board[3] == 'X' || board[2] == 'X' && board[4] == 'X' || board[7] == 'X' && board[8] == 'X')){
    board[6] = 'O';
  }
  else if(board[7] == '-' && (board[1] == 'X' && board[4] == 'X' || board[6] == 'X' && board[8] == 'X')){
    board[7] = 'O';
  }
  else if(board[8] == '-' && (board[0] == 'X' && board[4] == 'X' || board[2] == 'X' && board[5] == 'X' || board[6] == 'X' && board[7] == 'X')){
    board[8] = 'O';
  }

}

void mr_ai_man(char * board,int turn){

  finish_board_ai(board);
  //endplayer(board);

  if(board[4] == '-'){
    board[4] = 'O';
  }

  else{
    int r;
    r = corner();
    if(board[r] == '-'){
      board[r] = 'O';
      //r = corner();
    }
  }

  turn = 1;
}


int main(){
  int winner = 1;
  char path[3];
  char board[9];
  int player = 1;
  srand(time(0));

  //set up the board
  int c = 0;
  for(;c < 9;c++){
    board[c] = '-';
  }

  printf("Game Start! \nPlayer 1: X\nAI: O\nInput: 1-9 \n \n");
  printboard(board);

  while(winner){
    fgets(path,3,stdin);
    path[strlen(path)-1] = '\0';


    if(player == 1 && board[path[0]-49] == '-'){
      board[path[0]-49] = 'X';
      player = 2;
    }
    else if(board[path[0]-49 != '-']){
      printf("Space Taken \n");
    }

    //INSERT AI HERE
    mr_ai_man(board,player);
    player = 1;

    printf("\n");
    printboard(board);

    if(lastwinner(board)== 1 || checkwinner(board) == 1){
      winner = 0;
      printf("You won!\n");
    }

    if(lastwinner(board)== 2 || checkwinner(board) == 2){
      winner = 0;
      printf("You lost!\n");
    }
    else if(checkwinner(board) == 3){
      winner = 0;
      printf("Tie it up \n");
    }

  }
  return 0;
}
