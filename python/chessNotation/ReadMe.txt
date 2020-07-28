This script was made to get chess notation from "https://logic-games.spb.ru/chess/". 
There is no capability to copy chess notation fromthis site. By using this script you can 
import <body></body> part element and save it as *.txt

*.txt content must look like this:

<tbody>
	<tr>
		<td>1</td>
		<td data-nmove="1" class="chessHistoryActiveMove">e4</td>
		<td data-nmove="2" class="">e5</td>
	</tr>
	<tr>
		<td>2</td>
		<td data-nmove="3">Nf3</td>
		<td data-nmove="4">Nc6</td>
	</tr>
	<tr>
		<td>3</td>
		<td data-nmove="5">Nc3</td>
		<td data-nmove="6">Bc5</td>
	</tr>
	<tr>
		<td>4</td>
		<td data-nmove="7">Be2</td>
		<td data-nmove="8">Nd4</td>
	</tr>
	<tr>
		<td>5</td>
		<td data-nmove="9">Nxe5</td>
		<td data-nmove="10">Qf6</td>
	</tr>
	<tr>
		<td>6</td>
		<td data-nmove="11">Nf3</td>
		<td data-nmove="12">Nxf3+</td>
	</tr>
	<tr>
		<td>7</td>
		<td data-nmove="13">Bxf3</td>
		<td data-nmove="14">d6</td>
	</tr>
	<tr>
		<td>8</td>
		<td data-nmove="15">a3</td>
		<td data-nmove="16">Ne7</td>
	</tr>
	<tr>
		<td>9</td>
		<td data-nmove="17">b4</td>
		<td data-nmove="18">Bb6</td>
	</tr>
	<tr>
		<td>10</td>
		<td data-nmove="19">a4</td>
		<td data-nmove="20">O-O</td>
	</tr>
	<tr>
		<td>11</td>
		<td data-nmove="21">a5</td>
		<td data-nmove="22">Bd4</td>
	</tr>
	<tr>
		<td>12</td>
		<td data-nmove="23">h3</td>
		<td data-nmove="24">Bxc3</td>
	</tr>
	<tr>
		<td>13</td>
		<td data-nmove="25">dxc3</td>
		<td data-nmove="26">Qxc3+</td>
	</tr>
	<tr>
		<td>14</td>
		<td data-nmove="27">Qd2</td>
		<td data-nmove="28">Qxa1</td>
	</tr>
	<tr>
		<td>15</td>
		<td data-nmove="29">O-O</td>
		<td data-nmove="30">Qf6</td>
	</tr>
	<tr>
		<td>16</td>
		<td data-nmove="31">Re1</td>
		<td data-nmove="32">Ng6</td>
	</tr>
	<tr>
		<td>17</td>
		<td data-nmove="33">Qe3</td>
		<td data-nmove="34">Ne5</td>
	</tr>
	<tr>
		<td>18</td>
		<td data-nmove="35">Bd2</td>
		<td data-nmove="36">Nxf3+</td>
	</tr>
	<tr>
		<td>19</td>
		<td data-nmove="37">gxf3</td>
		<td data-nmove="38">Bxh3</td>
	</tr>
	<tr>
		<td>20</td>
		<td data-nmove="39">Bc3</td>
		<td data-nmove="40">Qg6+</td>
	</tr>
	<tr>
		<td>21</td>
		<td data-nmove="41">Kh2</td>
		<td data-nmove="42">Qg2#</td>
	</tr>
</tbody>

(!) Warning! No cyrillic symbols allowed!