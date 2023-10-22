using EventManagementService.Entities;

namespace EventManagementService.Repositories
{
    public interface IEventRepository
    {
        public Task<List<Event>> GetEventListAsync();
        public Task<Event> GetEventByIdAsync(int Id);
        public Task<Event> CreateEventAsync(Event newEvent);
        public Task<Event> UpdateEventAsync(Event updatedEvent);
        public Task<bool> DeleteEventAsync(int Id);
    }
}
