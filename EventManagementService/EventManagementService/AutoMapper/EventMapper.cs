using AutoMapper;
using EventManagementService.Entities;
using EventManagementService.Protos;
using System;

namespace EventManagementService.AutoMapper
{
    public class EventMapper : Profile
    {
        public EventMapper()
        {
            CreateMap<Event, EventDetails>().ReverseMap();
        }
    }
}
