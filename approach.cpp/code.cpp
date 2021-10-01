// C++ program to solve
// the given question

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Create class for hotel data.
class Hotel {
public:
	string name;
	int roomAvl;
	string location;
	int rating;
	int pricePr;
};

// Create class for user data.
class User : public Hotel {
public:
	string uname;
	int uId;
	int cost;
};

// Function to Sort Hotels by
// Bangalore location
bool sortByBan(Hotel& A, Hotel& B)
{
	return A.name > B.name;
}

// Function to sort hotels
// by rating.
bool sortByr(Hotel& A, Hotel& B)
{
	return A.rating > B.rating;
}

// Function to sort hotels
// by rooms availability.
bool sortByRoomAvailable(Hotel& A,
						Hotel& B)
{
	return A.roomAvl < B.roomAvl;
}

// Print hotels data.
void PrintHotelData(vector<Hotel> hotels)
{
	cout << "PRINT HOTELS DATA:" << endl;
	cout << "HotelName"
		<< " "
		<< "Room Available"
		<< " "
		<< "Location"
		<< " "
		<< "Rating"
		<< " "
		<< "PricePer Room:" << endl;

	for (int i = 0; i < 3; i++) {
		cout << hotels[i].name
			<< "		 "
			<< hotels[i].roomAvl
			<< "			 "
			<< hotels[i].location
			<< "	 "
			<< hotels[i].rating
			<< "		 "
			<< hotels[i].pricePr
			<< endl;
	}
	cout << endl;
}

// Sort Hotels data by name.
void SortHotelByName(vector<Hotel> hotels)
{
	cout << "SORT BY NAME:" << endl;

	std::sort(hotels.begin(), hotels.end(),
			sortByBan);

	for (int i = 0; i < hotels.size(); i++) {
		cout << hotels[i].name << " "
			<< hotels[i].roomAvl << " "
			<< hotels[i].location << " "
			<< hotels[i].rating << " "
			<< " " << hotels[i].pricePr
			<< endl;
	}
	cout << endl;
}

// Sort Hotels by rating
void SortHotelByRating(vector<Hotel> hotels)
{
	cout << "SORT BY A RATING:" << endl;

	std::sort(hotels.begin(),
			hotels.end(), sortByr);

	for (int i = 0; i < hotels.size(); i++) {
		cout << hotels[i].name << " "
			<< hotels[i].roomAvl << " "
			<< hotels[i].location << " "
			<< hotels[i].rating << " "
			<< " " << hotels[i].pricePr
			<< endl;
	}
	cout << endl;
}

// Print Hotels for any city Location.
void PrintHotelBycity(string s,
					vector<Hotel> hotels)
{
	cout << "HOTELS FOR " << s
		<< " LOCATION IS:"
		<< endl;
	for (int i = 0; i < hotels.size(); i++) {

		if (hotels[i].location == s) {

			cout << hotels[i].name << " "
				<< hotels[i].roomAvl << " "
				<< hotels[i].location << " "
				<< hotels[i].rating << " "
				<< " " << hotels[i].pricePr
				<< endl;
		}
	}
	cout << endl;
}

// Sort hotels by room Available.
void SortByRoomAvailable(vector<Hotel> hotels)
{
	cout << "SORT BY ROOM AVAILABLE:" << endl;

	std::sort(hotels.begin(), hotels.end(),
			sortByRoomAvailable);

	for (int i = hotels.size() - 1; i >= 0; i--) {

		cout << hotels[i].name << " "
			<< hotels[i].roomAvl << " "
			<< hotels[i].location << " "
			<< hotels[i].rating << " "
			<< " " << hotels[i].pricePr
			<< endl;
	}
	cout << endl;
}

// Print the user's data
void PrintUserData(string userName[],
				int userId[],
				int bookingCost[],
				vector<Hotel> hotels)
{

	vector<User> user;
	User u;

	// Access user data.
	for (int i = 0; i < 3; i++) {
		u.uname = userName[i];
		u.uId = userId[i];
		u.cost = bookingCost[i];
		user.push_back(u);
	}

	// Print User data.
	cout << "PRINT USER BOOKING DATA:"
		<< endl;
	cout << "UserName"
		<< " "
		<< "UserID"
		<< " "
		<< "HotelName"
		<< " "
		<< "BookingCost" << endl;

	for (int i = 0; i < user.size(); i++) {
		cout << user[i].uname
			<< "		 "
			<< user[i].uId
			<< "	 "
			<< hotels[i].name
			<< "		 "
			<< user[i].cost
			<< endl;
	}
}

// Functiont to solve
// Hotel Management problem
void HotelManagement(string userName[],
					int userId[],
					string hotelName[],
					int bookingCost[],
					int rooms[],
					string locations[],
					int ratings[],
					int prices[])
{
	// Initialize arrays that stores
	// hotel data and user data
	vector<Hotel> hotels;

	// Create Objects for
	// hotel and user.
	Hotel h;

	// Initialise the data
	for (int i = 0; i < 3; i++) {
		h.name = hotelName[i];
		h.roomAvl = rooms[i];
		h.location = locations[i];
		h.rating = ratings[i];
		h.pricePr = prices[i];
		hotels.push_back(h);
	}
	cout << endl;

	// Call the various operations
	PrintHotelData(hotels);
	SortHotelByName(hotels);
	SortHotelByRating(hotels);
	PrintHotelBycity("Bangalore",
					hotels);
	SortByRoomAvailable(hotels);
	PrintUserData(userName,
				userId,
				bookingCost,
				hotels);
}

// Driver Code.
int main()
{

	// Initialize variables to stores
	// hotels data and user data.
	string userName[] = { "U1", "U2", "U3" };
	int userId[] = { 2, 3, 4 };
	string hotelName[] = { "H1", "H2", "H3" };
	int bookingCost[] = { 1000, 1200, 1100 };
	int rooms[] = { 4, 5, 6 };
	string locations[] = { "Bangalore",
						"Bangalore",
						"Mumbai" };
	int ratings[] = { 5, 5, 3 };
	int prices[] = { 100, 200, 100 };

	// Function to perform operations
	HotelManagement(userName, userId,
					hotelName, bookingCost,
					rooms, locations,
					ratings, prices);

	return 0;
}
