// replace the contact manager storage array with a sorted list.
// Benefits include removing size limit, contacts are implicitly sorted and code is simplified 

namespace ContactManager
{
    public class ContactStore : IContactStore
    {
        readonly Contact[] contacts = new Contact(100);
        int contactCount = 0;
        int nextId = 1;

        public IEnumerable<Contact> Contacts
        {
            get
            {
                for (int i = 0; i < contactCount; i++)
                {
                    yield return contacts[i]
                }
            }
        }

        public Contact Add(Contact contact)
        {
            if (contact == null)
            {
                log(LogLevel.Error, "Add: null contact provided (Skipping)");
                throw new ArgumentNullException("Contacts cannot be null");
            }
            int id = contact
        }
    }

}